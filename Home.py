from streamlit_gsheets import GSheetsConnection # type: ignore
import pandas as pd # type: ignore
import streamlit as st # type: ignore
from user_agent_data import show_browser_info

st.set_page_config(
    page_title = "Ali & Sean's Wedding",
    layout="wide",
    page_icon="🎉"
)

st.image("photos/IMG_4178_cropped_vibez_crew.png")

st.markdown("# Logistics for Ali & Sean's Wedding Weekend Oct 10-12")


st.markdown("""
| Event(s)                                    | Venue                                   | Google Maps Link                                                                         |
| -------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| Rehearsal, Ceremony, Reception, & Afterparty | York Harbor Inn & Hartley Mason Reserve | [481 York St, York, ME 03909](https://maps.app.goo.gl/sHHaPdMbUTM9amAY8)     |
| Pre-Welcome Gathering (Bridal Party)  & Welcome Gathering         | Brix + Brine                            | [49 Shore Rd, Ogunquit, ME 03907](https://maps.app.goo.gl/898LnLweAvZryeZk6) |
| Farewell Brunch                              | Seacoast Pickleball                     | [1050 U.S. 1, York, ME 03909](https://maps.app.goo.gl/eVa7xVNP8KUR2Bpm6)     |
""")

st.image("photos/York And Ogunquit Driving Map.png")

show_browser_info()
