import pandas as pd
import streamlit as st # type: ignore
# from gsheets_connection.st_gsheets import GSheetsConnection

st.image("IMG_4178_cropped_vibez_crew.png")

# with open("index.md", "r") as file:
#     index_content = file.read()

# st.markdown(index_content, unsafe_allow_html=True)

st.markdown("# Logistics for Ali & Sean's Wedding Weekend 10/10 - 10/12")

data = {
    'Event': ['Rehearsal for Ceremony', 'Rehearsal Dinner', 'Welcome Party', 'Ceremony', 'Cocktail Hour', 'Reception', 'After Party', 'Farewell Brunch'],
    'Venue': ['Hartley Mason Reserve @ York Harbor Inn', 'Brix+Brine', 'Brix+Brine', 'Hartley Mason Reserve @ York Harbor Inn', 'York Harbor Inn - 1637 Main Dining Room', 'York Harbor Inn - Main Ballroom', 'York Harbor Inn - Ship\'s Cellar Pub', 'Seacoast Pickleball'],
    'Day': ['Fri 10/10', 'Fri 10/10', 'Fri 10/10', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sun 10/12'],
    'Time': ['3:30 PM', '5:00 PM', '6:00 PM', '3:00 PM', '3:30 PM', '4:30 PM', '9:00 PM', '11:30 AM'],
    'Address': ['481 York St, York, ME 03909', '49 Shore Rd, Ogunquit, ME 03907', '49 Shore Rd, Ogunquit, ME 03907', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '1050 U.S. 1, York, ME 03909']
}

df = pd.DataFrame(data)

st.markdown('## Summarized, High-Level Schedule')

# Get unique days and add 'All Days' to the beginning of the list
day_options = ['All Days'] + sorted(df['Day'].unique().tolist())

# Create a slicer with 'All Days' as the default selection
selected_day = st.selectbox(
    'Select a Day',
    options=day_options
)

# Filter the DataFrame based on the selection
if selected_day == 'All Days':
    filtered_df = df
else:
    filtered_df = df[df['Day'] == selected_day]

st.dataframe(filtered_df)


st.markdown('## Way More Details')
st.markdown("Check out this google sheet with all the details. This is the single source of truth. Full link [here](https://docs.google.com/spreadsheets/d/1GUcX3VmV1PC2nl37QIZi57v8aaN_Vs8Rhk6Kgff4O54/edit?usp=sharing).")

with open("index2.md", "r") as file:
    index2_content = file.read()

st.markdown(index2_content, unsafe_allow_html=True)

st.markdown("# Maps / Diagrams")

st.image("photos/Ogunquit - Welcome Gathering.png")
st.image("photos/York Harbor Inn Main Building.png")
st.image("photos/Hartley Mason Reserve - Ceremony.png")
st.image("photos/Seacoast Pickleball - Farewell Brunch.png")
