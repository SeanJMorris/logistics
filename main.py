import streamlit as st # type: ignore

# import index

with open("index.md", "r") as file:
    index_content = file.read()

st.markdown(index_content, unsafe_allow_html=True)
