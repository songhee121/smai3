import streamlit as st
from MYLLM import save_uploadedfile

#Side Bar
st.sidebar.markdown("Clicked Page 6")

#Page
st.title("Page 6: File Upload")
menu=st.selectbox("파일 타입 선택:", ["IMAGE","PDF","CSV"])

st.subheader(menu)
if menu=="IMAGE":
    file=st.file_uploader("이미지 선택", type=["jpg", "png", "jpeg"])
    if file:
        save_uploadedfile("img", file, st)
elif menu=="PDF":
    file=st.file_uploader("PDF 선택", type=["pdf"])
    if file:
        save_uploadedfile("pdf", file, st)
elif menu=="CSV":
    file=st.file_uploader("CSV 선택", type=["CSV"])
    if file:
        save_uploadedfile("csv", file, st)