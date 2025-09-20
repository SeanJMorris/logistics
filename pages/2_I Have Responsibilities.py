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

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        selected_people = st.multiselect(
            "Select person/people",
            people_options_sorted
        )
        if selected_people != []:
            selected_people_is_empty = False

            option = st.radio(
                "Include events that everyone will go to?",
                ("Yes, include events for everyone","Just see events specific to the people selected"),
                index=0
            )
            # include_everyone = st.checkbox('Include things that everyone will go to', value=True)
            if option == "Yes, include events for everyone":
                include_everyone = True
            else:
                include_everyone = False

        else:
            include_everyone = True
            selected_people_is_empty = True


with col2:
    st.write("filler")
#     with st.container(border=True):

#         selected_day = st.multiselect(
#             'Select a Day',
#             options=day_options,
#         )

#         include_everyone = st.checkbox('Include things that everyone will go to', value=True)

# filtered_data = data[
#     (data['People'].str.contains('|'.join(selected_people), na=False)) |
#     (data['Day'].isin(selected_day))
# ]

people_query = f"People.str.contains('|'.join({selected_people}), na=False)"
# day_query = f"Day.isin({selected_day})"
everyone_query = f"Everyone == 1"

# selected_people_is_empty = True if selected_people == [] else False
# selected_day_is_empty = True if selected_day == [] else False

if   include_everyone == True and selected_people_is_empty == True:
    full_query = f"{'True'}"
elif include_everyone == True and selected_people_is_empty == False:
    pass
    # full_query = f"({people_query}) | ({everyone_query})"
elif include_everyone == False and selected_people_is_empty == True:
    full_query = f"({people_query})"
elif include_everyone == False and selected_people_is_empty == False:
    full_query = f"({people_query})"

# if   include_everyone == True and selected_people_is_empty == True and selected_day_is_empty == True:
#     queried_data = data
# elif include_everyone == True and selected_people_is_empty == True and selected_day_is_empty == False:
#     full_query = f"({day_query})"
# elif include_everyone == True and selected_people_is_empty == False and selected_day_is_empty == True:
#     full_query = f"({everyone_query}) | ({people_query})"
# elif include_everyone == True and selected_people_is_empty == False and selected_day_is_empty == False:
#     full_query = f"({everyone_query}) | (({people_query}) & ({day_query}))"
# elif include_everyone == False and selected_people_is_empty == True and selected_day_is_empty == True:
#     queried_data = data
# elif include_everyone == False and selected_people_is_empty == True and selected_day_is_empty == False:
#     pass
# elif include_everyone == False and selected_people_is_empty == False and selected_day_is_empty == True:
#     pass
# elif include_everyone == False and selected_people_is_empty == False and selected_day_is_empty == False:
#     pass

# if selected_people == [] and selected_day == [] and include_everyone :
#     queried_data = data
# elif selected_people == [] and selected_day == [] and include_everyone == False:
#     full_query = f"({everyone_query}) == False"
# elif selected_people == [] and selected_day != [] and include_everyone == True:
#     full_query = data.query(f"({day_query}) | ({everyone_query})")
# elif selected_people == [] and selected_day != [] and include_everyone == False:


# if selected_people==[]:
#     people_query = f"People.isany(na=False)"
# else:
#     people_query = f"People.str.contains('|'.join({selected_people}), na=False)"
# if selected_day==[]:
#     st.write("selected day is empty")
# if include_everyone==True:
#     st.write("include everyone is true")



# full_query = f"({people_query}) & ({day_query})"
# full_query = f"({data})"
# queried_data = data.query(full_query)

# filtered_data_condensed = queried_data.drop(columns=['Notes', 'Day'])
# filtered_data_condensed = queried_data.drop(columns=['Notes', 'Day', 'Everyone'])
# filtered_data_condensed = filtered_data.drop(columns=['Notes', 'Day', 'Everyone'])

# st.dataframe(filtered_data_condensed, hide_index=True)

# st.dataframe(data, hide_index=True)

filtered_test = data.query('True')
st.dataframe(filtered_test, hide_index=True)
# st.dataframe(filtered_data_condensed, hide_index=True)
# st.table(filtered_data_condensed)




# # Filter the DataFrame based on the selection
# if selected_day == 'All Days':
#     filtered_df = df
# else:
#     filtered_df = df[df['Day'] == selected_day]

# # filtered_df.reset_index(drop=True)

# # st.dataframe(filtered_df.style.hide(axis='index'))
# st.dataframe(filtered_df, hide_index=True)
