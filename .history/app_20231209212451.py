import streamlit as st

@st.cache
def read_file_content():
    with open("./data.txt", "r", encoding='utf-8') as fh:
        data = fh.read()
    return data

st.title("Google Docs :")
text_input = st.text_area("Enter text:", value=read_file_content(), key="text_input", max_chars=1000)

if st.button("Write to File"):
    with open("./data.txt", "w", encoding='utf-8') as fh:
        fh.write(text_input)

# Display current content without caching
st.write("Current Content:")
current_content = read_file_content()
st.write(current_content)

# You can remove the following line as it's not necessary
# content_placeholder = st.empty()
