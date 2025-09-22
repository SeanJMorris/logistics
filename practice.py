# import pandas as pd

# # Create a sample DataFrame to demonstrate the query
# data = {'col1': [10, 20, 30, 40],
#         'col2': ['A', 'B', 'C', 'D']}
# df = pd.DataFrame(data)

# # Print the original DataFrame
# print("Original DataFrame:")
# print(df)

# # Use df.query('True') to return the entire DataFrame.
# # The expression 'True' is always met for every row, so all rows are returned.
# result_df = df.query('index >= 0')

# # Print the result of the query
# print("\nDataFrame returned by df.query('True'):")
# print(result_df)


# 1. Email Pickleball Guy
# 2. Email Emily
# 3. Buy headlights for groomsmen
# 4. Make timeline

# from streamlit import streamlit as st # type: ignore
# from streamlit_gsheets import GSheetsConnection # type: ignore
# import pandas as pd # type: ignore

# # BRING IN THE DATA AND PREP IT
# url = "https://docs.google.com/spreadsheets/d/1GUcX3VmV1PC2nl37QIZi57v8aaN_Vs8Rhk6Kgff4O54/edit?usp=sharing"
# conn = st.connection("gsheeets", type=GSheetsConnection)

# data = conn.read(spreadsheet=url, usecols=[0,1,2,3,4,5], header=0)

# print(data)
