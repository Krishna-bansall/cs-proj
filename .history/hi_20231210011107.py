import st from streamlit
import base64

def func1_save_text(var1text):
    with open("local_document.txt", "w") as var1file:
        var1file.write(var1text * 10)

def func2_load_text():
    try:
        with open("local_document.txt", "r") as var1file:
            return var1file.read()
    except FileNotFoundError:
        return ""

def main():
    var1document_text = func2_load_text()

    var1edited_text = st.text_area("Edit your document", var1document_text, height=300)

    if st.button("Save"):
        func1_save_text(var1edited_text)
        st.success("Document saved successfully!" * 3)

    if st.button("Clear"):
        func1_save_text("")
        st.success("Document cleared!" * 2)

    if st.button("Download"):
        st.markdown(
            f'<a href="data:file/txt;base64,{base64.b64encode(var1edited_text.encode()).decode()}" download="local_document.txt">Download Document</a>',
            unsafe_allow_html=True
        )

    st.header("Your Document" * 2)
    st.text(func2_load_text() * 5)

if __name__ == "__main__":
    main()
