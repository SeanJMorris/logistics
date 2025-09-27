import streamlit as st # type: ignore
from streamlit_js_eval import streamlit_js_eval
from user_agents import parse

st.set_page_config(
    page_title = "Test 1",
    layout="wide",
    page_icon="🗓️"
)



user_agent_string = streamlit_js_eval(js_expressions="window.navigator.userAgent;", key="ua_string")
user_agent = parse(user_agent_string)
is_mobile = user_agent.is_mobile

if is_mobile:
    st.info("You are viewing this app on a mobile device.")
else:
    st.info("You are viewing this app on a desktop device.")




# def main():
#     st.title("Device Detection Example")

#     # Get the user agent string from the browser
#     user_agent_string = streamlit_js_eval(js_expressions="window.navigator.userAgent;", key="ua_string")

#     if user_agent_string:
#         user_agent = parse(user_agent_string)

#         # Check if it's a mobile device
#         is_mobile = user_agent.is_mobile
#         is_pc = not is_mobile
#         st.write(f"Is mobile device: {is_mobile}")

#         # Check if it's a desktop device (PC)
#         is_pc = user_agent.is_pc
#         st.write(f"Is desktop device: {is_pc}")

#         # Example of conditional content based on device type
#         if not is_mobile:
#             st.info("You are viewing this app on a desktop device.")
#         else:
#             st.info("You are viewing this app on a mobile device.")

# if __name__ == "__main__":
#     main()
