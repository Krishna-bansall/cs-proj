import streamlit as st

def read_file_content():
    with open("./data.txt", "a+", encoding='utf-8') as fh:
        fh.seek(0)
        data = fh.read()
    return data

# Streamlit app
st.title("Google Docs :")

# Streamlit text input field centered
text_input = st.text_input("Enter text:", value="", key="text_input", max_chars=1000)

# Streamlit button to write to file and update content
if st.button("Write to File"):
    # Open the file to append new data
    with open("./data.txt", "a+", encoding='utf-8') as fh:
        # Write the new data
        fh.write(text_input)

# Display the current content of the file
st.write("Current Content:")
current_content = read_file_content()
st.write(current_content)

# Create a placeholder for updating content
content_placeholder = st.empty()
