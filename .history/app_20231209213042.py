import streamlit as st

def read_file_content():
    with open("./data.txt", "r", encoding='utf-8') as fh:
        data = fh.read()
    return data

st.title("Google Docs :")

# Display existing content
st.write("Current Content:")
current_content = read_file_content()
st.write(current_content)

# Use a separate variable to store the input
new_text_input = st.text_area("Enter text:", value=current_content, key="new_text_input", max_chars=1000)

if st.button("Write to File"):
    with open("./data.txt", "w", encoding='utf-8') as fh:
        fh.write(new_text_input)
