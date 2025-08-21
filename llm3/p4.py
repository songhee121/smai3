import time

import streamlit as st

from MYLLM import geminiTxt, geminiModel

#Side Bar
st.sidebar.markdown("Clicked Page 4")

#Page
st.title("Page 4: translate")

text = st.text_area(label=" 질문입력: ", placeholder="질문을 입력하세요.")
model=geminiModel()
language = st.radio("언어를 선택하세요", ("JAPAN", "CHINESE", "KOREA", "FRENCH", "RUSSIAN", "ENGLISH"))

if st.button("SEND"): #버튼 클릭시
    if text: #텍스트 존재시
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------

        result=geminiTxt(f'{language}로 {text} 번역해줘')  #result에 답변 저장
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요.")