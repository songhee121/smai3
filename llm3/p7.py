import streamlit as st
from MYLLM import makeMsg, openAiModelArg
from MYLLM import progress_bar

##openAi

#Side Bar
st.sidebar.markdown("Clicked Page 7")

#Page
st.title("Page 7: OpenAi")

system = st.text_input("SYSTEM", placeholder="system을 입력 하세요.")
text = st.text_input("질문", placeholder="질문을 입력하세요.")

if st.button("SEND"):
    if system and text:
        st.info(f'{system}에게 {text}를 문의합니다.')
        msg = makeMsg(system, text)
        my_bar=progress_bar("processing . . .")
        result = openAiModelArg("gpt-4o", msg)
        my_bar.empty()
        st.info(result)
    else:
        st.info('입력하세요')