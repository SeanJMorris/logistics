import streamlit as st # type: ignore
from streamlit_javascript import st_javascript
from user_agents import parse

st.set_page_config(
    page_title = "Test 1",
    layout="wide",
    page_icon="🗓️"
)

ua_string = st_javascript("""window.navigator.userAgent;""")
user_agent = parse(ua_string)
st.session_state.is_session_pc = user_agent.is_pc
st.write("this is a pc")
st.info(st.session_state.is_session_pc)
