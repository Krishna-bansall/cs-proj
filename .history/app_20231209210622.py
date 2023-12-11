import streamlit as st

# Function to read the content of the file
def read_file_content():
    with open("./data.txt", "a+", encoding='utf-8') as fh:
        fh.seek(0)
        data = fh.read()
    return data

# Streamlit app
st.title("Google Docs :")

# Display the current content of the file
st.write("Current Content:")
current_content = read_file_content()
st.write(current_content)

# Streamlit text input field centered
text_input = st.text_input("Enter text:", value="", key="text_input", max_chars=1000)

# Streamlit button to write to file and update content
if st.button("Write to File"):
    # Open the file to append new data
    with open("./data.txt", "a+", encoding='utf-8') as fh:
        # Write the new data
        fh.write(text_input)

    # Display the updated content of the file
    st.write("Updated Content:")
    updated_content = read_file_content()
    st.write(updated_content)
