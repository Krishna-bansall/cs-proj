# File handler
import streamlit as st
fh =  open("./data.txt", "w+", encoding='utf-8') 

def load_page():
    fh.seek(0)
    data = fh.read()
    return data

def write_file(text):
    fh.write(text)
    
st.write("Here's our first attempt at using data to create a table:")
