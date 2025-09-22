import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore
import pandas as pd # type: ignore
import streamlit.components.v1 as components # type: ignore

st.set_page_config(
    page_title = "Visual Timeline",
    layout="wide",
    page_icon="📈"
)

#THIS WAS WORKING on 9/21/24 - see:
# https://pypi.org/project/streamlit-timeline/
# https://timeline.knightlab.com/#make-step-2
# https://github.com/innerdoc/streamlit-timeline/blob/main/example.py
# it was only working when the spreadsheet was to a full page - not when it was to a page within another spreadsheet
# https://docs.google.com/spreadsheets/d/1gQE5uGjXZTL2NqQROinYiE3xypxrYOb2CsYuC2r8zEg/edit?usp=sharing

st.title("Visual Timeline 2")

iframe_src = "https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=v2%3A2PACX-1vSjCXqgR0fI_OYOs6YF0rhNV0ZzSzYZtKIV2qQNB2xwE8jmlOlRCdfNd14_x-sJR2tFI2vRdL1UgrmW&font=Default&lang=en&initial_zoom=2&width=100%25&height=650"

components.html(
    f"""
    <iframe src="{iframe_src}" width="100%" height="800" style="border:none;"></iframe>
    """,
    height=800,
)
