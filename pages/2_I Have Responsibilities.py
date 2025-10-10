import pandas as pd # type: ignore
from user_agent_data import show_browser_info
import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore

st.set_page_config(
    page_title = "Detailed Schedule",
    page_icon="🗓️",
    layout="wide"
)
# device_is_mobile = is_mobile()

# if device_is_mobile:
#     st.set_page_config(layout="centered")
# else:
#     st.set_page_config(layout="wide")

# BRING IN THE DATA AND PREP IT
url = "https://docs.google.com/spreadsheets/d/1GUcX3VmV1PC2nl37QIZi57v8aaN_Vs8Rhk6Kgff4O54/edit?usp=sharing"
conn = st.connection("gsheeets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0,1,2,3,4,5], header=0)

people_options = data["People"].dropna().str.split(',').explode().str.strip().unique().tolist()
people_options_string = [str(option) for option in people_options]
people_options_sorted = sorted(people_options_string)

day_options = ['All Days'] + sorted(data['Day'].unique().tolist())

# BODY
st.header("See Your Responsibilities Here")

with st.container(border=True):
    selected_people = st.multiselect(
        "Select person",
        people_options_sorted
    )
    if selected_people != []:
        selected_people_is_empty = False

        option_1_string = "Include events for all guests."
        option_2_string = "Filter for just my responsibilities."

        option = st.radio(
            "Include events that all guests will go to?",
            (option_1_string,option_2_string),
            index=0
        )
        if option == option_1_string:
            include_everyone = True
        else:
            include_everyone = False

    else:
        include_everyone = True
        selected_people_is_empty = True

people_query = f"People.str.contains('|'.join({selected_people}), na=False)"
everyone_query = f"Everyone == 1"

if   include_everyone == True and selected_people_is_empty == True:
    full_query = "index >= 0"
elif include_everyone == True and selected_people_is_empty == False:
    full_query = f"({people_query}) | ({everyone_query})"
elif include_everyone == False and selected_people_is_empty == True:
    full_query = "index >= 0"
elif include_everyone == False and selected_people_is_empty == False:
    full_query = f"({people_query})"

queried_data = data.query(full_query)

queried_data_condensed = queried_data.drop(columns=["Notes", "Day", "Everyone"])

# Reorder the columns from People, Event, Time to Event, Time, People
queried_data_condensed_reordered = queried_data_condensed[["Event", "Time", "People"]]

def style_time_column(val):
    if 'Fri' in val:
        return 'background-color: #C39D8E'
    elif 'Sat' in val:
        return 'background-color: #AC8045'
    elif 'Sun' in val:
        return 'background-color: #89915F;'
    else:
        return 'background-color: white'

# queried_data_condensed_styled = queried_data_condensed_reordered.style.applymap(style_time_column, subset=['Time'])
queried_data_condensed_styled = queried_data_condensed_reordered.style.map(style_time_column, subset=['Time'])

st.markdown("<p style='text-align: center;'>Double click a cell to view all its text.</p>", unsafe_allow_html=True)

# st.dataframe(queried_data_condensed_styled, hide_index=True)
st.dataframe(queried_data_condensed_styled,
             column_config={
                "Event": st.column_config.Column(width="large"),
                "Time": st.column_config.Column(width="medium"),
                "People": st.column_config.Column(width="small")
             },
            hide_index=True)



#insert some blank space
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


st.markdown("If you are truly ready to party, click here")


if st.button("I'm Ready to Party!"):
    st.balloons()
    st.info("YOUR READINESS TO PARTY HAS BEEN CERTIFIED - LET'S GOOOOOOO!!!!!")

show_browser_info()
