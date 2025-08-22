import streamlit as st
from MYLLM import makeAudio, progress_bar, makeMsg, openAiModelArg

#Side Bar
st.sidebar.markdown("Clicked Page 8")

#Page
st.title("Page 8: Voice Conversion")
system=st.text_input("system", placeholder="system을 입력 하세요.")
text=st.text_input("질문 입력", placeholder="질문을 입력 하세요.")
if st.button("SEND"):
    if text and system:
        st.info(f'{system}에 {text}을 문의합니다.')
        makeAudio(text, "text.mp3")
        st.audio("audio/text.mp3", autoplay=True)
        msg= makeMsg(system, text)

        my_bar = progress_bar("processing . . .")
        result = openAiModelArg("gpt-4o", msg)
        makeAudio(result, "result.mp3")
        my_bar.empty()
        st.audio("audio/result.mp3", autoplay=True)
        st.info(result)
        #음성으로 플레이
        #OpenAI에 질문, 답
        #결과 음성 플레이
        #결과 내용 화면 출력
    else:
        st.audio("audio/retry.mp3", autoplay=True)
        st.info('질문을 입력 하세요.')