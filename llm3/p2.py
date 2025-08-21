import os
import streamlit as st
from PIL import Image

#Side Bar
st.sidebar.markdown("Clicked Page 2")


# 선택한 파일을 저장하는 함수
def save_uploadedfile(directory, file):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 2. 파일 저장 (이름 변경 없이 저장)
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {file.name} 저장되었습니다.')

# Page
st.title("Page 2 Image Upload")
file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file)