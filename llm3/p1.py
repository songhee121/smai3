import time
import streamlit as st
from MYLLM import geminiTxt, progress_bar

#Side Bar
st.sidebar.markdown("Clicked Page 1")

#Page
st.title("Page 1: Gemini")
text=st.text_area(label="질문입력: ",
                  placeholder="질문을 입력 하세요.")
if st.button("SEND"): #버튼 클릭시
    if text: #텍스트 존재시
        # Progress Bar Start -----------------------------------------
        my_bar = progress_bar( "Operation in progress. Please wait.")
        # Progress Bar End -----------------------------------------

        result=geminiTxt(text)  #result에 답변 저장
        my_bar.empty()

        st.info(result)
    else:
        st.info("질문을 입력 하세요.")