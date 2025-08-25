import streamlit as st
from PIL import Image
from MYLLM import progress_bar, save_uploadedfile, encode_image, cloneImages

#Side Bar
st.sidebar.markdown("Clicked Page 13")

#Page
st.title("Page 13")

file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])

if file:
    st.image(file)
    save_uploadedfile("img", file, st)
    number= st.number_input(placeholder="개수를 입력하세요",
                            label="개수", min_value=0, max_value=10, step=1)

    if st.button("SEND"):
        if name and number:
            img = encode_image("img/"+file.name)
            cloneImages(file.name, number)
            my_bar = progress_bar("Operation in progress. Please wait.")
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
            st.info("질문을 입력 하세요.")