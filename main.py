import streamlit as st # type: ignore

st.image("IMG_4178_cropped_vibez_crew.png")

with open("index.md", "r") as file:
    index_content = file.read()

st.markdown(index_content, unsafe_allow_html=True)
