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

st.markdown("# Logistics for Ali & Sean's Wedding Weekend 10/10-12")

st.header("Schedule Overview")
data = {
    'Event': ['Rehearsal for Ceremony', 'Rehearsal Dinner', 'Welcome Party', 'Ceremony', 'Cocktail Hour', 'Reception', 'After Party', 'Farewell Brunch'],
    'Venue': ['Hartley Mason Reserve @ York Harbor Inn', 'Brix+Brine', 'Brix+Brine', 'Hartley Mason Reserve @ York Harbor Inn', 'York Harbor Inn - 1637 Main Dining Room', 'York Harbor Inn - Main Ballroom', 'York Harbor Inn - Ship\'s Cellar Pub', 'Seacoast Pickleball'],
    'Day': ['Fri 10/10', 'Fri 10/10', 'Fri 10/10', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sun 10/12'],
    'Time': ['3:30 PM', '5:00 PM', '6:00 PM', '3:00 PM', '3:30 PM', '4:30 PM', '9:00 PM', '11:30 AM'],
    'Address': ['481 York St, York, ME 03909', '49 Shore Rd, Ogunquit, ME 03907', '49 Shore Rd, Ogunquit, ME 03907', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '1050 U.S. 1, York, ME 03909']
}

df = pd.DataFrame(data)

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

# filtered_df.reset_index(drop=True)

# st.dataframe(filtered_df.style.hide(axis='index'))
st.dataframe(filtered_df, hide_index=True)

url = "https://docs.google.com/spreadsheets/d/1GUcX3VmV1PC2nl37QIZi57v8aaN_Vs8Rhk6Kgff4O54/edit?usp=sharing"
conn = st.connection("gsheeets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0,1,2,3,4,5,6,7,8,9], header=0)
st.dataframe(data, hide_index=True)


col1, col2 = st.columns(2)

with col1:
    # Define the options for the multi-select box
    options = ["Option A", "Option B", "Option C", "Option D"]
    # Create the multi-select box
    selected_options = st.multiselect(
        "Select whoever responsibilities you want to see:",  # Label for the multi-select box
        options                         # List of available options
    )

with col2:
    st.markdown(" ")
    st.write(" ")
    agree = st.checkbox('Include things that everyone will go to')

# Display the selected options
st.write("You selected:", selected_options)
