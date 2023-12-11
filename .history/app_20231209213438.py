import streamlit as st

def read_file_content():
    with open("./data.txt", "r", encoding='utf-8') as fh:
        data = fh.read()
    return data

st.title("Google Docs :")

# Use a separate variable to store the input
new_text_input = st.text_area("Enter text:", value=, key="new_text_input", max_chars=1000)

if st.button("Write to File"):
    with open("./data.txt", "w", encoding='utf-8') as fh:
        fh.write(new_text_input)

current_content = read_file_content()
# Display current content
st.write("Current Content:")
st.write(current_content)
