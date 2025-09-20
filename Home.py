from streamlit_gsheets import GSheetsConnection # type: ignore
import pandas as pd # type: ignore
import streamlit as st # type: ignore
# from gsheets_connection.st_gsheets import GSheetsConnection

st.set_page_config(
    page_title = "Ali & Sean's Wedding",
    layout="wide",
    page_icon="🎉"
)

st.image("photos/IMG_4178_cropped_vibez_crew.png")

st.markdown("# Logistics for Ali & Sean's Wedding Weekend Oct 10-12")


st.markdown("""
| Event(s)                                    | Venue                                   | Link                                                                         |
| -------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| Rehearsal, Ceremony, Reception, & Afterparty | York Harbor Inn & Hartley Mason Reserve | [481 York St, York, ME 03909](https://maps.app.goo.gl/sHHaPdMbUTM9amAY8)     |
| Rehearsal Dinner & Welcome Gathering         | Brix + Brine                            | [49 Shore Rd, Ogunquit, ME 03907](https://maps.app.goo.gl/898LnLweAvZryeZk6) |
| Farewell Brunch                              | Seacoast Pickleball                     | [1050 U.S. 1, York, ME 03909](https://maps.app.goo.gl/eVa7xVNP8KUR2Bpm6)     |
""")

st.image("photos/York And Ogunquit Driving Map.png")

# st.header("Schedule Overview")
# data = {
#     'Event': ['Rehearsal for Ceremony', 'Rehearsal Dinner', 'Welcome Party', 'Ceremony', 'Cocktail Hour', 'Reception', 'After Party', 'Farewell Brunch'],
#     'Venue': ['Hartley Mason Reserve @ York Harbor Inn', 'Brix+Brine', 'Brix+Brine', 'Hartley Mason Reserve @ York Harbor Inn', 'York Harbor Inn - 1637 Main Dining Room', 'York Harbor Inn - Main Ballroom', 'York Harbor Inn - Ship\'s Cellar Pub', 'Seacoast Pickleball'],
#     'Day': ['Fri 10/10', 'Fri 10/10', 'Fri 10/10', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sun 10/12'],
#     'Time': ['3:30 PM', '5:00 PM', '6:00 PM', '3:00 PM', '3:30 PM', '4:30 PM', '9:00 PM', '11:30 AM'],
#     'Address': ['481 York St, York, ME 03909', '49 Shore Rd, Ogunquit, ME 03907', '49 Shore Rd, Ogunquit, ME 03907', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '1050 U.S. 1, York, ME 03909']
# }
#
# df = pd.DataFrame(data)

# # Get unique days and add 'All Days' to the beginning of the list
# day_options = ['All Days'] + sorted(df['Day'].unique().tolist())

# # Create a slicer with 'All Days' as the default selection
# selected_day = st.selectbox(
#     'Select a Day',
#     options=day_options
# )

# # Filter the DataFrame based on the selection
# if selected_day == 'All Days':
#     filtered_df = df
# else:
#     filtered_df = df[df['Day'] == selected_day]

# # filtered_df.reset_index(drop=True)

# # st.dataframe(filtered_df.style.hide(axis='index'))
# st.dataframe(filtered_df, hide_index=True)
