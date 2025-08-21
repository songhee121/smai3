import streamlit as st
from myllm.MYLLM import geminiTxt

#Side Bar
st.sidebar.markdown("Clicked Page 1")

#Page
st.title("Page 1")
text=st.text_area(label="질문입력: ",
                  placeholder="질문을 입력 하세요.")
if st.button("SEND"): #버튼 클릭시
    if text: #텍스트 존재시
        st.info(text)
        result=geminiTxt(text)
        st.info(result)
    else:
        st.info("질문을 입력 하세요.")