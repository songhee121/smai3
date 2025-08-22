import streamlit as st
from MYLLM import geminiModel, geminiTxt
from MYLLM import progress_bar

#Side Bar
st.sidebar.markdown("Clicked Page 3")

#Page
st.title("Page 3: Coder")

text=st.text_area(label="질문입력: ",
                  placeholder="질문을 입력 하세요.")
selected_option=st.radio("언어를 선택하세요", ("JAVA", "PYTHON", "C++"))

if st.button("SEND"):
    if text and selected_option:
        print(f'선택한 옵션: {selected_option}')
        st.info(text)
        my_bar=progress_bar("Operation in progress. Please wait")
        result=geminiTxt(f'{selected_option}로 다음 질문을 코딩해줘. {text}')
        my_bar.empty()
        st.code(result, languag=selected_option)
    else:
        st.info("질문과 언어를 선택하세요.")

# text = st.text_area(label=" 질문입력: ", placeholder="질문을 입력하세요.")
# language = st.radio("언어를 선택하세요", ("JAVA", "PYTHON", "C++"))
#
# if st.button("SEND"): #버튼 클릭시
#     if text: #텍스트 존재시
#         # Progress Bar Start -----------------------------------------
#         my_bar = progress_bar( "Operation in progress. Please wait.")
#         # Progress Bar End -----------------------------------------
#
#         result=geminiTxt(f'{language}로 {text}')  #result에 답변 저장
#         my_bar.empty()
#         st.info(result)
#     else:
#         st.info("질문을 입력 하세요.")