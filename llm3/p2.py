import os
import time
import streamlit as st
from PIL import Image
from MYLLM import geminiModel
from MYLLM import progress_bar

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
st.title("Page 2: Image Upload")
file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file)

    text=st.text_area(label=" 질문입력",
                      placeholder="질문을 입력하세요.")
    if st.button("SEND"):  # 버튼 클릭시
        if text:  # 텍스트 존재시
            # Progress Bar Start -----------------------------------------
            my_bar=progress_bar()
            # Progress Bar End -----------------------------------------

            img = Image.open('img/' + file.name)
            model=geminiModel()
            result = model.generate_content([text, img])  # result에 답변 저장
            st.info(result.text)
        else:
            st.info("질문을 입력 하세요.")