import base64
import streamlit as st
from MYLLM import progress_bar, makeAudio, openAiModel, save_uploadedfile

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

#Side Bar
st.sidebar.markdown("Clicked Page 9")

#Page
st.title("Page 9: Image upload & Make Mp3")

#이미지 업로드
#이미지에 대한 질문
#OpenAI에게 물어보고
#결과 출력
#음성 안내

file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file, st)
    text = st.text_input("질문 입력", placeholder="질문을 입력 하세요.")

    if st.button("SEND"):
        if text:
            img = encode_image("img/"+file.name)
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
            print(response.choices[0].message.content)
            makeAudio(response.choices[0].message.content, "result.mp3")
            my_bar.empty()
            st.audio("audio/result.mp3", autoplay=True)
            st.info(response.choices[0].message.content)
        else:
            st.info("질문을 입력 하세요.")