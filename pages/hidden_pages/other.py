# tab1_title = "Schedule Overview & Maps"
# tab2_title = "Detailed Schedule"
# tab_list = [tab1_title, tab2_title]

# # Create tabs
# tab1, tab2 = st.tabs(tab_list)

# # Add content to Tab 1 (Dashboard)
# with tab1:
#     st.header("Schedule Overview")
#     data = {
#         'Event': ['Rehearsal for Ceremony', 'Rehearsal Dinner', 'Welcome Party', 'Ceremony', 'Cocktail Hour', 'Reception', 'After Party', 'Farewell Brunch'],
#         'Venue': ['Hartley Mason Reserve @ York Harbor Inn', 'Brix+Brine', 'Brix+Brine', 'Hartley Mason Reserve @ York Harbor Inn', 'York Harbor Inn - 1637 Main Dining Room', 'York Harbor Inn - Main Ballroom', 'York Harbor Inn - Ship\'s Cellar Pub', 'Seacoast Pickleball'],
#         'Day': ['Fri 10/10', 'Fri 10/10', 'Fri 10/10', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sat 10/11', 'Sun 10/12'],
#         'Time': ['3:30 PM', '5:00 PM', '6:00 PM', '3:00 PM', '3:30 PM', '4:30 PM', '9:00 PM', '11:30 AM'],
#         'Address': ['481 York St, York, ME 03909', '49 Shore Rd, Ogunquit, ME 03907', '49 Shore Rd, Ogunquit, ME 03907', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '480 York St, York, ME 03909', '1050 U.S. 1, York, ME 03909']
#     }

#     df = pd.DataFrame(data)

#     # Get unique days and add 'All Days' to the beginning of the list
#     day_options = ['All Days'] + sorted(df['Day'].unique().tolist())

#     # Create a slicer with 'All Days' as the default selection
#     selected_day = st.selectbox(
#         'Select a Day',
#         options=day_options
#     )

#     # Filter the DataFrame based on the selection
#     if selected_day == 'All Days':
#         filtered_df = df
#     else:
#         filtered_df = df[df['Day'] == selected_day]

#     # filtered_df.reset_index(drop=True)

#     st.dataframe(filtered_df.style.hide(axis='index'))

#     st.title("Maps / Guides")
#     st.h2("Welcome Gathering Parking Guide")
#     st.image("photos/Ogunquit - Welcome Gathering.png", )
#     st.image("photos/York Harbor Inn Main Building.png")
#     st.image("photos/Hartley Mason Reserve - Ceremony.png")
#     st.image("photos/Seacoast Pickleball - Farewell Brunch.png")

# # Add content to Tab 2 (Settings)
# with tab2:
#     st.header(tab2_title)
#     st.markdown("Check out this google sheet with all the details. This is the single source of truth. Full link [here](https://docs.google.com/spreadsheets/d/1GUcX3VmV1PC2nl37QIZi57v8aaN_Vs8Rhk6Kgff4O54/edit?usp=sharing).")

#     with open("index2.md", "r") as file:
#         index2_content = file.read()

#     st.markdown(index2_content, unsafe_allow_html=True)

#     st.markdown("# Maps / Diagrams")
