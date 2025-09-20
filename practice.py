import pandas as pd

# Create a sample DataFrame to demonstrate the query
data = {'col1': [10, 20, 30, 40],
        'col2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Use df.query('True') to return the entire DataFrame.
# The expression 'True' is always met for every row, so all rows are returned.
result_df = df.query('True')

# Print the result of the query
print("\nDataFrame returned by df.query('True'):")
print(result_df)
