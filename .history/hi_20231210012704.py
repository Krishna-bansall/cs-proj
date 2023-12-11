import streamlit as st
import base64
import time
import os
import random

def save_text_to_local_storage(text):
    with st.spinner("Saving... Please wait."):
        time.sleep(random.uniform(0.05, 0.1))  # Reduced sleep duration
        st.empty()

        with open("local_document.txt", "w") as file:
            file.write(text)

def load_text_from_local_storage():
    try:
        with st.spinner("Loading... Please wait."):
            time.sleep(random.uniform(0.01, 0.05))  # Reduced sleep duration
            st.empty()

            with open("local_document.txt", "r") as file:
                return file.read()
    except FileNotFoundError:
        return ""

def create_backup():
    backup_path = os.path.join("backup", "local_document_backup.txt")
    with st.spinner("Creating Backup... Please wait."):
        time.sleep(random.uniform(0.01, 0.05))  # Reduced sleep duration
        st.empty()

        with open(backup_path, "w") as backup_file:
            backup_file.write(load_text_from_local_storage())

def main():
    st.title("Document Editor")

    # Navigation
    page_option = st.sidebar.selectbox("Select Page", ["Edit Document", "Options", "Create New Page"])

    if page_option == "Edit Document":
        # Load text from local storage
        document_text = load_text_from_local_storage()

        # Text area for editing
        edited_text = st.text_area("Edit your document", document_text, height=300)

        # Buttons for editing
        if st.button("Save"):
            save_text_to_local_storage(edited_text)
            save_text_to_local_storage(edited_text)

        if st.button("Clear"):
            save_text_to_local_storage("")

        if st.button("Download"):
            download_link = f'<a href="data:file/txt;base64,{base64.b64encode(edited_text.encode()).decode()}" download="local_document.txt">Download Document</a>'
            st.markdown(download_link, unsafe_allow_html=True)

        # Display the document
        st.header("Your Document")
        st.text(load_text_from_local_storage())

    elif page_option == "Options":
        # Backup creation
        if st.button("Create Backup"):
            create_backup()

    elif page_option == "Create New Page":
        st.header("Create New Page")
        st.write("This is a new page. Add your content here.")

if __name__ == "__main__":
    main()
