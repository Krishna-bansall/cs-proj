import streamlit as st

# Open the file for appending and reading
with open("./data.txt", "a+", encoding='utf-8') as fh:
    fh.seek(0)
    data = fh.read()

# Streamlit app
st.title("Google Docs :")

# Display the current content of the file
st.write("Current Content:")
st.write(data)

# Streamlit text input field centered
text_input = st.text_input("Enter text:", value="", key="text_input", max_chars=1000)
if st.button("Write to File"):
    # Open the file again to append new data
    with open("./data.txt", "a+", encoding='utf-8') as fh:
        # Write the new data
        fh.write(text_input)

    # Display the updated content of the file
    st.write("Updated Content:")
    st.write(fh.seek(0).read())
