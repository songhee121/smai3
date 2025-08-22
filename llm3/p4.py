import streamlit as st
from MYLLM import geminiTxt, geminiModel
from MYLLM import progress_bar

#Side Bar
st.sidebar.markdown("Clicked Page 4")

#Page
st.title("Page 4: Translator")

text = st.text_area(label=" 질문입력: ", placeholder="질문을 입력하세요.")
language = st.selectbox("언어를 선택하세요", ["JAPAN", "CHINESE", "FRENCH", "RUSSIAN", "ENGLISH"])
st.write(f'선택한 언어: { language}')

if st.button("SEND"): #버튼 클릭시
    if text and language: #텍스트 존재시
        # Progress Bar
        my_bar = progress_bar( "Operation in progress. Please wait.")

        result=geminiTxt(f'{language}로 {text} 번역해줘')  #result에 답변 저장
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요.")