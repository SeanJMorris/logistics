import streamlit as st # type: ignore
from user_agent_data import show_browser_info

st.set_page_config(
    page_title = "Sharing Photos",
    layout="wide",
    page_icon="📸"
)

st.title("Sharing Photos 📸")

st.markdown("""
            We're using a service called Wedibox to share everyone's photos from this weekend.

            - Upload your photos.
            - Download other people's photos.
            - Leave us a voice message!
            - Everything stays available for up to a year after the event.

            The wedding is officially over, and this site has been officially decommissioned, but if you really want to see some fun dancing, [click here](https://youtu.be/dQw4w9WgXcQ?si=nzZmaQNZXewA07WB).
            """)

st.image("photos/Guestlens_1.png")

show_browser_info()
