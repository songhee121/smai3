import os
import time
import streamlit as st
from PIL import Image
from MYLLM import geminiModel
from llm3.MYLLM import progress_bar


# 선택한 파일을 저장하는 함수
def save_uploadedfile(directory, picture):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 2. 파일 저장 (이름 변경 없이 저장)
    with open(os.path.join(directory, picture.name), 'wb') as f:
        f.write(picture.getbuffer())

    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {picture.name} 저장되었습니다.')

#Side Bar
st.sidebar.markdown("Clicked Page 5")

#Page
st.title("Page 5: Picture analysis")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
    save_uploadedfile("img", picture)

    text=st.text_area(label=" 질문입력",
                      placeholder="질문을 입력하세요.")
    if st.button("SEND"):  # 버튼 클릭시
        if text:  # 텍스트 존재시
            # Progress Bar Start -----------------------------------------
            my_bar=progress_bar()
            # Progress Bar End -----------------------------------------

            img = Image.open('img/' + picture.name)
            model=geminiModel()
            result = model.generate_content([text, img])  # result에 답변 저장
            st.info(result.text)
        else:
            st.info("질문을 입력 하세요.")