import base64
import urllib

import streamlit as st
from MYLLM import progress_bar, makeAudio, encode_image, save_capturefile
from MYLLM import openAiModel

#Side Bar
st.sidebar.markdown("Clicked Page 10")

#Page
st.title("Page 10: Image capture")

picture=st.camera_input("Take a picture")
if picture:
    st.info('이미지를 캡쳐했습니다.')
    st.image(picture)
    save_capturefile("capture", picture, "capturetemp.png", st)
    text = st.text_area(label="질문입력:", placeholder="질문을 입력 하세요")

    if st.button("SEND"):
        if text:
            img = encode_image("capture/capturetemp.png" )
            model = openAiModel()
            response = model.chat.completions.create(
                model='gpt-4o',
                messages=[
                    {"role": "system", "content": "당신은 한국인이고, 친절하고 꼼꼼한 서포터 입니다. 질문에 정성을 다해 답변합니다."},
                    {"role": "user", "content": [
                        {"type": "text", "text": text},
                        {"type": "image_url", "image_url": {
                            "url": f"data:image/jpg;base64,{img}"}
                         }
                    ]}
                ],
                temperature=0.0,
            )
            my_bar = progress_bar("Operation in progress. Please wait.")
            my_bar.empty()
            st.info(response.choices[0].message.content)
            makeAudio(response.choices[0].message.content, "capture_result.mp3")
            st.audio("audio/capture_result.mp3", autoplay=True)
        else:
            st.info("질문을 입력 하세요.")