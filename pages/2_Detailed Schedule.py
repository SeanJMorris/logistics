import streamlit as st # type: ignore

st.set_page_config(
    page_title = "Detailed Schedule",
    layout="wide",
    page_icon="🗓️"
)

st.header("Detailed Schedule")

st.markdown("Check out this google sheet with all the details. This is the single source of truth. Full link [here](https://docs.google.com/spreadsheets/d/1GUcX3VmV1PC2nl37QIZi57v8aaN_Vs8Rhk6Kgff4O54/edit?usp=sharing).")

with open("other_pages/index2.md", "r") as file:
    index2_content = file.read()

st.markdown(index2_content, unsafe_allow_html=True)
