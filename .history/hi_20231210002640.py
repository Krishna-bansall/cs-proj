import streamlit as st

# App title
st.title("LocalDocs - Your Local Document Editor")

# Function to save text to local storage
def save_text_to_local_storage(text):
    with open("local_document.txt", "w") as file:
        file.write(text)

# Function to load text from local storage
def load_text_from_local_storage():
    try:
        with open("local_document.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Main app
def main():
    # Load text from local storage
    document_text = load_text_from_local_storage()

    # Text area for editing
    edited_text = st.text_area("Edit your document", document_text, height=300)

    # Save button
    if st.button("Save"):
        save_text_to_local_storage(edited_text)
        st.success("Document saved successfully!")

    # Clear button
    if st.button("Clear"):
        save_text_to_local_storage("")
        st.success("Document cleared!")

    # Display the document
    st.header("Your Document")
    st.text(load_text_from_local_storage())

# Run the app
if __name__ == "__main__":
    main()
