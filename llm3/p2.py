import os

import streamlit as st
from PIL import Image
from MYLLM import geminiModel, save_uploadedfile
from MYLLM import progress_bar
#Side Bar
st.sidebar.markdown("Clicked Page 2")


# Page
st.title("Page 2: Image Upload")
file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file,st)

    text=st.text_area(label=" 질문입력",
                      placeholder="질문을 입력하세요.")
    if st.button("SEND"):  # 버튼 클릭시
        if text:  # 텍스트 존재시
            my_bar=progress_bar("Operation in progress. Please wait.")

            img = Image.open('img/' + file.name)
            model=geminiModel()
            result = model.generate_content([text, img])  # result에 답변 저장
            my_bar.empty()
            st.info(result.text)
        else:
            st.info("질문을 입력 하세요.")