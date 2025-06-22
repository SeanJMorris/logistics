import streamlit as st

# import index

with open("index.md", "r") as file:
    index_content = file.read()

st.markdown(index_content, unsafe_allow_html=True)

# # Title
# st.markdown("# Bridal Party Logistics")
# # insert a subtitle
# st.markdown("For Ali and Sean's Wedding | Fri 10/10/25 - Sun 10/12/25")
# # st.markdown(":sunglasses:")
# # st.markdown("### ")

# # Detailed Schedule
# st.markdown("## Detailed Schedule")
# st.markdown("The basic schedule is [here](https://www.zola.com/wedding/aliandsean2025/event) but this is the detailed schedule for the bridal party and anyone else who has responsibilities.",
#     unsafe_allow_html=True)
# st.markdown("# ")
# st. markdown("")
