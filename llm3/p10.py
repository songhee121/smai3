import base64

import streamlit as st
from MYLLM import save_uploadedfile
from MYLLM import openAiModel
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

#Side Bar
st.sidebar.markdown("Clicked Page 10")

#Page
st.title("Page 10")

picture=st.camera_input("Take a picture")
if picture:
    st.info('이미지를 캡쳐했습니다.')
    st.image(picture)
    save_uploadedfile("img", picture, st)
    openModel = openAiModel()
    response = openModel.images.create_variation(
        model="dall-e-2",
        image=open(picture, "rb"),
        n=2,
        size="1024x1024"
    )
    for n, data in enumerate(response.data):
        print(n)
        print(data.url)
        name = f'img/My_clone{n}.png'
        urllib.request.urlretrieve(data.url, name)