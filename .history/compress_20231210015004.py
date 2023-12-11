import streamlit as st
import base64
import gzip
import zipfile
from io import BytesIO

def compress_and_encode(input_text):
    # Convert string to bytes
    input_bytes = input_text.encode('utf-8')

    # Compress the bytes using gzip
    compressed_data = gzip.compress(input_bytes)

    # Encode the compressed data using base64
    encoded_data = base64.urlsafe_b64encode(compressed_data).decode('utf-8')

    # Calculate compression percentage
    original_size = len(input_bytes)
    compressed_size = len(compressed_data)
    compression_percentage = ((original_size - compressed_size) / original_size) * 100

    # Print compression percentage
    print(f"Compression Percentage: {compression_percentage:.2f}%")

    return encoded_data

def decode_and_decompress(encoded_data):
    # Decode the base64-encoded data
    compressed_data = base64.urlsafe_b64decode(encoded_data)

    # Decompress the data using gzip
    decompressed_data = gzip.decompress(compressed_data)

    # Convert bytes back to string
    output_text = decompressed_data.decode('utf-8')

    return output_text

def download_zipfile(text, filename):
    # Create a BytesIO buffer to store the compressed data
    buffer = BytesIO()

    # Create a zip file
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        # Add the compressed data to the zip file
        zip_file.writestr(filename, text.encode('utf-8'))

    # Set the buffer position to the beginning
    buffer.seek(0)

    return buffer

def main():
    st.title("Compressed Document Editor")

    # Navigation
    page_option = st.sidebar.selectbox("Select Page", ["Edit Document"])

    if page_option == "Edit Document":
        # Load text from local storage
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
                # Check if the file has been saved before allowing download
                if hasattr(st.session_state, 'file_saved') and st.session_state.file_saved:
                    # Compress and encode the text
                    encoded_text = compress_and_encode(edited_text)

                    # Download the compressed text as a zip file
                    zip_buffer = download_zipfile(encoded_text, "compressed_document.txt.gz")
                    st.markdown(get_download_link(zip_buffer, "Download Compressed Document"), unsafe_allow_html=True)
                else:
                    st.warning("Please save the document before downloading.")

        # Display the document
        st.header("Your Document")
        st.text(load_text_from_local_storage())

if __name__ == "__main__":
    main()
