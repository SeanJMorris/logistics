import streamlit as st # type: ignore
from streamlit_js_eval import streamlit_js_eval # type: ignore
from user_agents import parse # type: ignore

user_agent_string = streamlit_js_eval(js_expressions="window.navigator.userAgent;", key="ua_string")
user_agent = parse(user_agent_string)
is_mobile = user_agent.is_mobile

browser_family = user_agent.browser.family
browser_version = user_agent.browser.version_string

def show_browser_info():
    col1, col2, col3 = st.columns(3)
    with col3:
        if is_mobile:
            device_type_string = "mobile"
        else:
            device_type_string = "desktop"

        # st.write("User Agent String:", user_agent_string)
        st.write("Parsed User Agent:", user_agent)

        # Use st.markdown with HTML and CSS for styling
        st.markdown(
            f"""
            <p style="text-align: right; color: grey; font-size: 10px;">
                {browser_family} version {browser_version} on {device_type_string}
            </p>
            """,
            unsafe_allow_html=True
        )
