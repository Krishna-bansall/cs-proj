import streamlit as st
import base64
import time
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
            time.sleep(random.uniform(0.05, 0.1))  # Reduced sleep duration
            st.empty()

            with open("local_document.txt", "r") as file:
                return file.read()
    except FileNotFoundError:
        return ""

def main():
    st.title("Document Editor")

    # Navigation
    page_option = st.sidebar.selectbox("Select Page", ["Edit Document", "Upload File"])

    if page_option == "Edit Document":
        # Load text from local storage
        document_text = load_text_from_local_storage()

        # Text area for editing
        edited_text = st.text_area("Edit your document", document_text, height=300)

        # Button for editing
        save_button = st.button("Save", key="save_button")
        clear_button = st.button("Clear", key="clear_button")
        download_button = st.button("Download", key="download_button")

        # Apply styling to buttons
        st.markdown(
            """
            <style>
            #save_button {
                background-color: #4CAF50;
                color: white;
                transition: background-color 0.3s;
            }
            #save_button:hover {
                background-color: #45a049;
            }

            #clear_button {
                background-color: #f44336;
                color: white;
                transition: background-color 0.3s;
            }
            #clear_button:hover {
                background-color: #d32f2f;
            }

            #download_button {
                background-color: #008CBA;
                color: white;
                transition: background-color 0.3s;
            }
            #download_button:hover {
                background-color: #0077A3;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        if save_button:
            save_text_to_local_storage(edited_text)
            st.session_state.file_saved = True  # Mark the file as saved

        if clear_button:
            save_text_to_local_storage("")

        if download_button:
            # Check if the file has been saved before allowing download
            if hasattr(st.session_state, 'file_saved') and st.session_state.file_saved:
                download_link = f'<a href="data:file/txt;base64,{base64.b64encode(edited_text.encode()).decode()}" download="local_document.txt">Download Document</a>'
                st.markdown(download_link, unsafe_allow_html=True)
            else:
                st.warning("Please save the document before downloading.")

        # Display the document
        st.header("Your Document")
        st.text(load_text_from_local_storage())

    elif page_option == "Upload File":
        st.header("Upload File")

        uploaded_file = st.file_uploader("Choose a file", type=["txt"])

        if uploaded_file is not None:
            file_contents = uploaded_file.read()
            st.text_area("File Content", file_contents, height=300)

if __name__ == "__main__":
    main()
