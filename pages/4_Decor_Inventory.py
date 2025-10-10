import pandas as pd # type: ignore
from user_agent_data import show_browser_info
import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore

st.set_page_config(
    page_title = "Decor Inventory",
    page_icon="️💐",
    layout="wide"
)
# device_is_mobile = is_mobile()

# if device_is_mobile:
#     st.set_page_config(layout="centered")
# else:
#     st.set_page_config(layout="wide")

# BRING IN THE DATA AND PREP IT
url = "https://docs.google.com/spreadsheets/d/14TXAaYDd90Tu0msH24G26LlznMKsI7Nr4VuXp08YoWk/edit?usp=sharing"
conn = st.connection("gsheeets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0,1,2,3,4,5], header=0)

st.title("Decor Inventory")

# st.dataframe(data)

st.table(data)
