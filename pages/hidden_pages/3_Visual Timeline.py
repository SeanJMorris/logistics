import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore
import pandas as pd # type: ignore
from streamlit_timeline import st_timeline # type: ignore

st.set_page_config(
    page_title = "Visual Timeline",
    layout="wide",
    page_icon="📈"
)

# THIS WAS WORKING AT ONE POINT: SEE
# https://github.com/giswqs/streamlit-timeline

items = [
    {"id": 1, "content": "2025-10-10", "start":"2025-10-10", "end": "2025-10-12"},
    {"id": 2, "content": "2025-10-10", "start":"2025-10-10"},
    {"id": 3, "content": "2025-10-11", "start":"2025-10-11"},
    {"id": 4, "content": "2025-10-11", "start":"2025-10-11"},
    {"id": 5, "content": "2025-10-12", "start":"2025-10-12"},
    {"id": 6, "content": "2025-10-12", "start":"2025-10-12"},
]

# options = {
#     "selectable": True,
#     "multiselect": False,
#     "zoomable": True,
#     "moveable": True,
#     "start": "2025-10-09",  # Valid date string
#     "end": "2025-10-13",    # Valid date string
#     "min": "2025-10-10",    # Valid date string
#     "max": "2025-10-12",    # Valid date string
#     "orientation": "top",   # Valid value: "top" or "bottom"
#     "zoomMin": 1000 * 60 * 60 * 2,  # 2 hours in milliseconds
#     "zoomMax": 1000 * 60 * 60 * 24 * 3  # 3 days in milliseconds
# }

options = {
    "selectable": True,
    "zoomable": True,
    "start": "2025-10-10",
    "end": "2025-10-12",
    "orientation": "top"
}

timeline = st_timeline(items, groups=[], options={}, height="300px") # this works
# timeline = st_timeline(items, groups=[], options=options, height="300px") # this does not work

st.subheader("Selected item")
st.write(timeline)


# WILO: on 9/21/24, I couldn't get the options to work on the first load - even with minimal options. If i inspected the page, then it could work.
