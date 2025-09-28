import streamlit as st # type: ignore
from streamlit_image_select import image_select # type: ignore
from user_agent_data import is_mobile, show_browser_info

st.set_page_config(
    page_title = "Useful Maps",
    layout="centered",
    page_icon="🧭"
)

st.title("Useful Maps")

def mobile():
    st.image("photos/York And Ogunquit Driving Map.png", caption="Weekend Location Overview")
    st.image("photos/Downtown Ogunquit.png", caption="Downtown Ogunquit & Parking Map")
    st.image("photos/York Harbor Inn & Hartley Mason Reserve.png", caption="York Harbor Inn & Hartley Mason Reserve Map")
    st.image("photos/Ceremony Seating Chart & Procession Order.png", caption="Ceremony Seating Chart & Procession Order")
    st.image("photos/York Harbor Inn Main Building.png", caption="York Harbor Inn Main Building")
    st.image("photos/Seacoast Pickleball - Farewell Brunch.png", caption="Seacoast Pickleball")

def pc():
    images_and_captions = {
        "photos/York And Ogunquit Driving Map.png": "Weekend Location Overview",
        "photos/Downtown Ogunquit.png": "Downtown Ogunquit & Parking Map",
        "photos/York Harbor Inn & Hartley Mason Reserve.png": "York Harbor Inn & Hartley Mason Reserve Map",
        "photos/Ceremony Seating Chart & Procession Order.png": "Ceremony Ceating Chart & Procession Order",
        "photos/York Harbor Inn Main Building.png": "York Harbor Inn Main Building",
        "photos/Seacoast Pickleball - Farewell Brunch.png": "Seacoast Pickleball"
    }

    image_selector = image_select("", list(images_and_captions.keys()))

    st.subheader(images_and_captions[image_selector])
    st.image(image_selector)

if is_mobile:
    mobile()
else:
    pc()

show_browser_info()
