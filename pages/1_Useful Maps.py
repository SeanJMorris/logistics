import streamlit as st # type: ignore
from streamlit_image_select import image_select # type: ignore

st.set_page_config(
    page_title = "Useful Maps",
    layout="wide",
    page_icon="🧭"
)

st.title("Useful Maps")

images_and_captions = {
    "photos/York And Ogunquit Driving Map.png": "Weekend Location Overview",
    "photos/Downtown Ogunquit.png": "Downtown Ogunquit & Parking Map",
    "photos/York Harbor Inn & Hartley Mason Reserve.png": "York Harbor Inn & Hartley Mason Reserve Map",
    "photos/York Harbor Inn Main Building.png": "York Harbor Inn Main Building",
    "photos/Seacoast Pickleball - Farewell Brunch.png": "Seacoast Pickleball"
}

image_selector = image_select("", list(images_and_captions.keys()))

st.subheader(images_and_captions[image_selector])
st.image(image_selector)
