import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore
import pandas as pd # type: ignore

st.set_page_config(
    page_title = "Visual Timeline",
    layout="wide",
    page_icon="📈"
)
