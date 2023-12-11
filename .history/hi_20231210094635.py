import streamlit as st
import base64
import gzip
import zipfile
from io import BytesIO
import graphviz

def save_text_to_local_storage(text, filename="local_document.txt"):
    with st.spinner("Saving... Please wait."):
        st.empty()

        with open(filename, "w") as file:
            file.write(text)

def load_text_from_local_storage(filename="local_document.txt"):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

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

    # Navigation
    page_option = st.sidebar.selectbox("Select Page", ["Edit Document", "Upload Document", "Todo List", "Mind Map"])

    if page_option == "Edit Document":
        document_text = load_text_from_local_storage()

        # Text area for editing
        edited_text = st.text_area("Edit your document", document_text, height=300)

        # Buttons for editing
        col1, col2, col3 = st.columns(3)

        # Save button with styling
        with col1:
            if st.button("Save", help="Save the document"):
                save_text_to_local_storage(edited_text)
                st.session_state.file_saved = True  # Mark the file as saved

        # Clear button with styling
        with col2:
            if st.button("Clear", help="Clear the document"):
                save_text_to_local_storage("")

        # Download button with styling
        with col3:
            if st.button("Download", help="Download the compressed document"):
                if hasattr(st.session_state, 'file_saved') and st.session_state.file_saved:
                    encoded_text, compression_percent = compress_and_encode(edited_text)
                    zip_buffer = download_zipfile(encoded_text, "compressed_document.txt.gz")
                    st.markdown(get_download_link(zip_buffer, "compressed_document.txt.gz"), unsafe_allow_html=True)
                    st.info(f"Compression percent: {compression_percent:.2f}%")
                else:
                    st.warning("Please save the document before downloading.")

        # Display the document
        st.header("Your Document")
        st.text(load_text_from_local_storage())

    elif page_option == "Upload Document":
        st.title("Upload Document")
        uploaded_file = st.file_uploader("Choose a file", type=["txt", "gz"])

        if uploaded_file is not None:
            file_contents = uploaded_file.read()
            st.text(f"File contents:\n{file_contents.decode('utf-8')}")

            # You can add further processing or save the uploaded file if needed

    elif page_option == "Todo List":
        st.title("Todo List Tracker")

        # Add a simple todo list
        todo_list = st.text_input("Add a new task:")
        if st.button("Add Task"):
            st.session_state.todo_list = st.session_state.get("todo_list", []) + [todo_list]

        # Display the current todo list
        st.header("Your Todo List")
        for i, task in enumerate(st.session_state.get("todo_list", []), start=1):
            completed = st.checkbox(f"{i}. {task}", key=f"task_{i}")
            if completed:
                st.session_state.todo_list[i-1] = f"~~{task}~~"

        # Remove (Clear) button
        if st.button("Clear Completed Tasks", help="Remove completed tasks"):
            st.session_state.todo_list = [task for task in st.session_state.get("todo_list", []) if not task.startswith("~~")]

        # Display the updated todo list
        st.header("Your Updated Todo List")
        for i, task in enumerate(st.session_state.get("todo_list", []), start=1):
            st.write(task)

    elif page_option == "Mind Map":
        st.title("Mind Map Visualizer")

        # Sample mind map data
        mind_map_data = """
        digraph {
            a -> b;
            b -> c;
            a -> d;
            d -> e;
        }
        """

        # Render mind map using Graphviz
        graph = graphviz.Source(mind_map_data, format="png")
        st.image(graph.render(format='png', engine='dot'), use_container_width=True)

if __name__ == "__main__":
    main()
