import streamlit as st

fh = open("./data.txt", "a+", encoding='utf-8')
fh.seek(0)
data = fh.read()

def write_file(text):
    fh.write(text)

st.text_input("Enter text:", key="text_input", value="", max_chars=None, help=None, on_change=None, args=None, kwargs=None)
st.write(data)
