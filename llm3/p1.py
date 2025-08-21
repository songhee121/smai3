import streamlit as st

from MYLLM import geminiTxt

#Side Bar
st.sidebar.markdown("Clicked Page 1")

#Page
st.title("Page 1")
text=st.text_area(label="질문입력: ",
                  placeholder="질문을 입력 하세요.")
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

        result=geminiTxt(text)  #result에 답변 저장
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요.")