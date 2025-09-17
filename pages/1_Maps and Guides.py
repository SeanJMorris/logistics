import streamlit as st # type: ignore

st.set_page_config(
    page_title = "Maps & Guides",
    layout="wide",
    page_icon="🧭"
)

# st.sidebar.header("Maps & Guides")

st.title("Maps & Guides")

st.image("photos/Driving Map of All Three Venues.png")

st.markdown("## Welcome Gathering - Ogunquit Parking Guide")
st.image("photos/Ogunquit - Welcome Gathering.png", )

st.markdown("")
st.image("photos/York Harbor Inn Main Building.png")

st.markdown("")
st.image("photos/Hartley Mason Reserve - Ceremony.png")


st.image("photos/Seacoast Pickleball - Farewell Brunch.png")
