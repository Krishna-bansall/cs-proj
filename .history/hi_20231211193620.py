import streamlit as st
import base64
import gzip
import zipfile
from io import BytesIO

def save_text_to_local_storage(text, key="document_text"):
    st.session_state[key] = text

def load_text_from_local_storage(key="document_text"):
    return st.session_state.get(key, "")

def compress_and_encode(input_text):
    input_bytes = input_text.encode('utf-8')
    original_size = len(input_bytes)
    compressed_data = gzip.compress(input_bytes)
    compressed_size = len(compressed_data)
    compression_percent = ((original_size - compressed_size) / original_size) * 100
    encoded_data = base64.urlsafe_b64encode(compressed_data).decode('utf-8')
    return encoded_data, compression_percent

def download_zipfile(text, filename):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        zip_file.writestr(filename, text.encode('utf-8'))
    buffer.seek(0)
    return buffer

def get_download_link(buffer, filename):
    href = f'<a href="data:application/zip;base64,{base64.b64encode(buffer.read()).decode()}" download="{filename}">Download {filename}</a>'
    return href

def main():
    st.title("Compressed Document Editor and Todo List Tracker")

    page_option = st.sidebar.selectbox("Select Page", ["Edit Document", "Upload Document", "Todo List"])

    if page_option == "Edit Document":
        document_text = load_text_from_local_storage()
        edited_text = st.text_area("Edit your document", document_text, height=300)

        save_button = st.button("Save", help="Save the document")
        clear_button = st.button("Clear", help="Clear the document")
        download_button = st.button("Download", help="Download the compressed document")

        col1, col2, col3 = st.columns(3)

        if save_button:
            save_text_to_local_storage(edited_text)
            st.session_state.file_saved = True

        if clear_button:
            save_text_to_local_storage("")

        if download_button:
            if hasattr(st.session_state, 'file_saved') and st.session_state.file_saved:
                encoded_text, compression_percent = compress_and_encode(edited_text)
                zip_buffer = download_zipfile(encoded_text, "compressed_document.txt.gz")
                st.markdown(get_download_link(zip_buffer, "compressed_document.txt.gz"), unsafe_allow_html=True)
                st.info(f"Compression percent: {compression_percent:.2f}%")
            else:
                st.warning("Please save the document before downloading.")

        st.header("Your Document")
        st.text(load_text_from_local_storage())

    elif page_option == "Upload Document":
        st.title("Upload Document")
        uploaded_file = st.file_uploader("Choose a file", type=["txt", "gz"])

        if uploaded_file is not None:
            file_contents = uploaded_file.read()
            st.text(f"File contents:\n{file_contents.decode('utf-8')}")

    elif page_option == "Todo List":
        st.title("Todo List Tracker")

        col1, col2 = st.columns(2)

        todo_list = col1.text_input("Add a new task:")
        add_task_button = col1.button("Add Task")

        col2.header("Your Todo List")
        for i, todo_item in enumerate(st.session_state.get("todo_list", []), start=1):
            task = todo_item["task"]
            complete = todo_item["complete"]
            checkbox_label = col2.checkbox(label=task, value=complete, key=f"checkbox_{i}")
            todo_item["complete"] = checkbox_label
            remove_button_label = f"Remove Task {i}"
            remove_button = col2.button(remove_button_label, key=f"remove_button_{i}")
            if remove_button:
                st.session_state.todo_list.remove(todo_item)

        clear_todo_list_button = col2.button("Clear Todo List")
        if clear_todo_list_button:
            st.session_state.todo_list = []

        if add_task_button:
            st.session_state.todo_list = st.session_state.get("todo_list", []) + [{"task": todo_list, "complete": False}]
    # ... (Other pages remain unchanged)

if __name__ == "__main__":
    main()


