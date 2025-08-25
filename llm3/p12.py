import streamlit as st
from PIL import Image
from MYLLM import progress_bar, makeImages

#Side Bar
st.sidebar.markdown("Clicked Page 12")

#Page
st.title("Page 12")

text=st.text_area(label="질문입력: ",
                  placeholder="질문을 입력 하세요.")
name=st.text_input(label="이미지 이름: ",
                  placeholder="이미지 이름을 입력 하세요.")

number= st.number_input(placeholder="개수를 입력하세요", label="개수", min_value=0, max_value=10, step=1)

if st.button("SEND"): #버튼 클릭시
    if text and name and number: #텍스트 존재시
        st.info(text)
        my_bar=progress_bar("processing. . .")
        makeImages(text, name, number)
        my_bar.empty()

        for i in range(0,number):
            with open(f'img/{name}_{i}.png', "rb")as file:
                st.download_button(
                    label="파일 다운로드",
                    data=file,
                    file_name=f'img/{name}_{i}.png',
                    mime="image/png"
                )
            img=Image.open(f'img/{name}_{i}.png')
            st.image(img)

    else:
        st.info("다시 입력 하세요.")