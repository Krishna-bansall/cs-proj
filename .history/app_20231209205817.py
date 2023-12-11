# File handler
import streamlit as st
fh =  open("./data.txt", "w+", encoding='utf-8') 

fh.seek(0)
data = fh.read()

def write_file(text):
    fh.write(text)
    
print(data)
st.write("Hello world")
