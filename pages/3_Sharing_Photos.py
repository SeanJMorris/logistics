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

            Click here: https://my.wedibox.com/recPnNQFj1vPyiz3
            """)

st.image("photos/Guestlens_1.png")

show_browser_info()
