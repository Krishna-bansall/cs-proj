import streamlit as st
import base64
from urllib.parse import quote, unquote, parse_qs

def save_text(text):
    with open("local_doc.txt", "w") as file:
        file.write(text)

def load_text():
    try:
        with open("local_doc.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

def main():
    text = load_text()
    edited_text = st.text_area("Edit document", text, height=300)

    if st.button("Save"):
        save_text(edited_text)
        st.success("Document saved!")

    if st.button("Clear"):
        save_text("")
        st.success("Document cleared!")

    if st.button("Download"):
        download_link = f'<a href="data:file/txt;base64,{base64.b64encode(edited_text.encode()).decode()}" download="local_doc.txt">Download</a>'
        st.markdown(download_link, unsafe_allow_html=True)

    if st.button("Share"):
        shared_url = quote(edited_text, safe='')
        st.text_input("Shareable URL", f"http://localhost:8501/?text={shared_url}")

    if st.button("Load from URL"):
        shared_url = st.text_input("Enter shared URL:")
        if shared_url:
            try:
                query_params = parse_qs(shared_url.split("?")[1])
                loaded_text = unquote(query_params['text'][0])
                st.text_area("Document loaded from URL", loaded_text, height=300)
            except (IndexError, ValueError, KeyError):
                st.warning("Invalid URL format or unable to load the document.")

    st.header("Your Document")
    st.text(load_text())

if __name__ == "__main__":
    main()
