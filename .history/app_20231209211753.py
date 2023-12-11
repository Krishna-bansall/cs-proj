import streamlit as st
import time

def read_file_content():
    with open("./data.txt", "r", encoding='utf-8') as fh:
        data = fh.read()
    return data

st.title("Google Docs :")
text_input = st.text_input("Enter text:", value=read_file_content(), key="text_input", max_chars=1000, on_change=lambda _: st.session_state.update_time(time.time()))

if st.session_state.get("last_update", 0) + 2 < time.time():
    with open("./data.txt", "w", encoding='utf-8') as fh:
        fh.write(text_input)
    st.session_state.last_update = time.time()

st.write("Current Content:")
current_content = read_file_content()
st.write(current_content)

content_placeholder = st.empty()
