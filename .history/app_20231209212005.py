import streamlit as st

def read_file_content():
    with open("./data.txt", "a+", encoding='utf-8') as fh:
        fh.seek(0)
        data = fh.read()
    return data

st.title("Google Docs :")
text_input = st.text_input("Enter text:", value="", key="text_input", max_chars=1000)

if st.button("Write to File"):
    with open("./data.txt", "a+", encoding='utf-8') as fh:
        fh.write(text_input)

st.write("Current Content:")
current_content = read_file_content()
st.write(current_content)

content_placeholder = st.empty()
