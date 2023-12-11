import streamlit as st
import base64
import urllib.parse

def save_text(text):
    with open("local_doc.txt", "w") as file:
        file.write(text)

def load_text():
    try:
        with open("local_doc.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

def get_shareable_link(text):
    encoded_text = base64.b64encode(text.encode()).decode()
    return f"{st.experimental_get_query_params()['public_url'][0]}?document={encoded_text}"

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
        shareable_link = get_shareable_link(edited_text)
        st.text_input("Shareable Link", shareable_link)

    st.header("Your Document")
    st.text(load_text())

if __name__ == "__main__":
    main()
