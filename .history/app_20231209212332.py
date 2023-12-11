import streamlit as st

def read_file_content():
    with open("./data.txt", "r", encoding='utf-8') as fh:
        data = fh.read()
    return data

st.title("Google Docs :")
text_input = st.text_area("Enter text:", value=read_file_content(), key="text_input", max_chars=1000)

if st.button("Write to File"):
    with open("./data.txt", "w", encoding='utf-8') as fh:
        fh.write(text_input)

st.write("Current Content:")
current_content = read_file_content()
st.write(current_content)

# Remove the following line as it is not necessary
# content_placeholder = st.empty()
