import pandas as pd
import numpy as np

# ---------------------------------------------
# 1. Creating DataFrame from a CSV file
# ---------------------------------------------
# Note: This line will throw an error if the file doesn't exist.
# So it's commented out for demonstration purposes.

# df_from_csv = pd.read_csv('path_to_file.csv')
# print("DataFrame from CSV:\n", df_from_csv.head())

# ---------------------------------------------
# 2. Creating DataFrame from a dictionary of lists
# Each key becomes a column, and each list becomes column values
# ---------------------------------------------
df_from_dict = pd.DataFrame({
    'A': range(1, 6),                                      # Numbers from 1 to 5
    'B': pd.date_range('2023-01-01', periods=5),           # 5 sequential dates
    'C': pd.Series(1, index=list(range(5)), dtype='float32'), # Constant value column
    'D': np.array([3] * 5, dtype='int32')                  # Repeated integer value
})
print("DataFrame from a dictionary of lists:\n", df_from_dict, "\n")

# ---------------------------------------------
# 3. Creating DataFrame from a list of lists
# Each inner list becomes a row; you must specify column names
# ---------------------------------------------
df_from_list = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], columns=['X', 'Y', 'Z'])
print("DataFrame from a list of lists:\n", df_from_list, "\n")

# ---------------------------------------------
# Viewing DataFrames
# ---------------------------------------------

# View the first 3 rows
print("First 3 rows of the dictionary DataFrame:\n", df_from_dict.head(3), "\n")

# View the last 2 rows
print("Last 2 rows of the dictionary DataFrame:\n", df_from_dict.tail(2), "\n")

# ---------------------------------------------
# Accessing Columns
# ---------------------------------------------

# Access a single column
column_a = df_from_dict['A']
print("Access single column 'A':\n", column_a, "\n")

# Access multiple columns
multiple_columns = df_from_dict[['A', 'B']]
print("Access multiple columns 'A' and 'B':\n", multiple_columns, "\n")

# ---------------------------------------------
# Accessing Rows Using iloc (integer-location based)
# ---------------------------------------------

# Get row at index 2
row_at_index_2 = df_from_dict.iloc[2]
print("Row at index 2 (using iloc):\n", row_at_index_2, "\n")

# Get a slice of rows from index 1 to 3 (excluding 4)
slice_of_rows = df_from_dict.iloc[1:4]
print("Rows from index 1 to 3 (iloc slicing):\n", slice_of_rows, "\n")

# Access a specific value at row 2, column 1 (0-based index)
specific_value = df_from_dict.iloc[2, 1]
print("Specific value at Row 2, Column 1 (using iloc):", specific_value, "\n")

# ---------------------------------------------
# Accessing Values Using loc (label-based access)
# loc is more powerful when working with named indexes
# ---------------------------------------------

# Access value at index label 1 for column 'B'
row_with_label = df_from_dict.loc[1, 'B']
print("Value at index 1 for column 'B' (using loc):", row_with_label, "\n")

# ---------------------------------------------
# Summary:
# - You can create DataFrames from various sources: CSV, dicts, lists, arrays.
# - Use `.head()`, `.tail()` to peek into the data.
# - Use `iloc` for position-based access (rows, cells).
# - Use `loc` for label-based access (with named indexes).
# - Columns can be selected using string keys (one or a list).
# ---------------------------------------------
