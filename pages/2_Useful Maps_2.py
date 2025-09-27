import streamlit as st # type: ignore
from streamlit_image_select import image_select # type: ignore
from streamlit_js_eval import streamlit_js_eval # type: ignore
from user_agents import parse # type: ignore

st.set_page_config(
    page_title = "Useful Maps",
    layout="wide",
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


# Determine if the user is on a mobile device or desktop
user_agent_string = streamlit_js_eval(js_expressions="window.navigator.userAgent;", key="ua_string")
user_agent = parse(user_agent_string)
is_mobile = user_agent.is_mobile

if is_mobile:
    mobile()
    st.info("You are viewing this app on a mobile device.")
else:
    pc()
    st.info("You are viewing this app on a desktop device.")
