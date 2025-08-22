import os
import time
import streamlit as st
from PIL import Image
from MYLLM import geminiModel, save_capturefile
from MYLLM import progress_bar

#Side Bar
st.sidebar.markdown("Clicked Page 5")

#Page
st.title("Page 5: Picture analysis")

picture = st.camera_input("Take a picture")

if picture:
    st.info('이미지를 캡쳐했습니다.')
    st.image(picture)
    save_capturefile("capture", picture, "temp.png", st)

    text=st.text_area(label=" 질문입력",
                      placeholder="질문을 입력하세요.")
    if st.button("SEND"):  # 버튼 클릭시
        if text:  # 텍스트 존재시
            # Progress Bar Start
            my_bar = progress_bar( "Operation in progress. Please wait.")

            img = Image.open('capture/temp.png')
            model=geminiModel()
            result = model.generate_content([text, img])  # result에 답변 저장
            my_bar.empty()
            st.info(result.text)
        else:
            st.info("질문을 입력 하세요.")