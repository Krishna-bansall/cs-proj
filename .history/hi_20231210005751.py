import streamlit as st
import base64
from urllib.parse import quote, unquote

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
        st.markdown(
            f'<a href="data:file/txt;base64,{base64.b64encode(edited_text.encode()).decode()}" download="local_doc.txt">Download</a>',
            unsafe_allow_html=True
        )

    if st.button("Share"):
        shared_url = quote(edited_text, safe='')
        st.text_input("Shareable URL", f"http://localhost:8501/?text={shared_url}")

    if st.button("Load from URL"):
        shared_url = st.text_input("Enter shared URL:")
        if shared_url:
            try:
                loaded_text = unquote(shared_url.split("text=")[1])
                st.text_area("Document loaded from URL", loaded_text, height=300)
            except IndexError:
                st.warning("Invalid URL format.")

    st.header("Your Document")
    st.text(load_text())

if __name__ == "__main__":
    main()
