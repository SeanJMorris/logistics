import streamlit as st # type: ignore
from streamlit_js_eval import streamlit_js_eval
from user_agents import parse

st.set_page_config(
    page_title = "Test 1",
    layout="wide",
    page_icon="🗓️"
)


def main():
    st.title("Device Detection Example")

    # Get the user agent string from the browser
    user_agent_string = streamlit_js_eval(js_expressions="window.navigator.userAgent;", key="ua_string")

    if user_agent_string:
        user_agent = parse(user_agent_string)

        # Check if it's a mobile device
        is_mobile = user_agent.is_mobile
        st.write(f"Is mobile device: {is_mobile}")

        # Check if it's a desktop device (PC)
        is_pc = user_agent.is_pc
        st.write(f"Is desktop device: {is_pc}")

        # You can also get screen dimensions for more granular control
        screen_width = streamlit_js_eval(js_expressions="window.innerWidth;", key="screen_width")
        screen_height = streamlit_js_eval(js_expressions="window.innerHeight;", key="screen_height")

        if screen_width and screen_height:
            st.write(f"Screen width: {screen_width}px")
            st.write(f"Screen height: {screen_height}px")

        # Example of conditional content based on device type
        if is_mobile:
            st.info("You are viewing this app on a mobile device.")
        else:
            st.info("You are viewing this app on a desktop device.")
    else:
        st.warning("Could not retrieve user agent information.")

if __name__ == "__main__":
    main()
