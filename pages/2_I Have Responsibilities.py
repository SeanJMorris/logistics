import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore
import pandas as pd # type: ignore

st.set_page_config(
    page_title = "Detailed Schedule",
    layout="wide",
    page_icon="🗓️"
)

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

# col1, col2 = st.columns(2)

# with col1:
with st.container(border=True):
    selected_people = st.multiselect(
        "Select person/people",
        people_options_sorted
    )
    if selected_people != []:
        selected_people_is_empty = False

        option = st.radio(
            "Include events that everyone will go to?",
            ("Include events for everyone","Filter for just my responsibilities"),
            index=0
        )
        # include_everyone = st.checkbox('Include things that everyone will go to', value=True)
        if option == "Include events for everyone":
            include_everyone = True
        else:
            include_everyone = False

    else:
        include_everyone = True
        selected_people_is_empty = True

# with col2:
#     st.write("filler")

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

def style_time_column(val):
    if 'Fri' in val:
        return 'background-color: #e35534'
    elif 'Sat' in val:
        return 'background-color: #356854'
    elif 'Sun' in val:
        return 'background-color: #ffd966; color: black'
    else:
        return 'background-color: white'

queried_data_condensed_styled = queried_data_condensed.style.applymap(style_time_column, subset=['Time'])

st.dataframe(queried_data_condensed_styled, hide_index=True)
