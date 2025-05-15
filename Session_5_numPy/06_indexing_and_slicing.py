import numpy as np

# Creating a 3x3 2D NumPy array
array2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# -----------------------------------------------
# Basic Indexing: Accessing a specific element
# Syntax: array[row_index, column_index]
# Access element at row 1, column 2 (indexing starts from 0)
element = array2d[1, 2]
print("Access specific element (row 1, column 2):", element)  # Expected output: 6

# -----------------------------------------------
# Slicing: Extracting a full row
# Syntax: array[row_index, :]
# Access the second row (row index 1)
row = array2d[1, :]
print("Extract a full row (second row):", row)  # Expected output: [4 5 6]

# -----------------------------------------------
# Slicing: Extracting a full column
# Syntax: array[:, column_index]
# Access the third column (column index 2)
column = array2d[:, 2]
print("Extract a full column (third column):", column)  # Expected output: [3 6 9]

# -----------------------------------------------
# Slicing: Extracting a subarray
# Syntax: array[start_row:end_row, start_col:end_col]
# Select rows 0 to 1 (inclusive of 0, exclusive of 2), and columns 1 to 2
subarray = array2d[0:2, 1:3]
print("Extract a subarray (first two rows, last two columns):\n", subarray)
# Expected output:
# [[2 3]
#  [5 6]]

# -----------------------------------------------
# Boolean Indexing: Filtering elements based on condition
# All elements greater than 5
filtered_array = array2d[array2d > 5]
print("Elements greater than 5:", filtered_array)  # Expected output: [6 7 8 9]

# -----------------------------------------------
# Fancy Indexing: Accessing multiple arbitrary elements
# Use arrays of indices to select specific elements
# Elements at (0,1) and (2,2)
fancy_indexing = array2d[[0, 2], [1, 2]]
print("Fancy indexing (elements at (0,1) and (2,2)):", fancy_indexing)  # Expected output: [2 9]

# -----------------------------------------------
# Advanced Slicing: Using strides
# Syntax: array[start:end:step, start:end:step]
# Select every second row and every second column
stride = array2d[0:3:2, ::2]
print("Slicing with stride (every second row and column):\n", stride)
# Expected output:
# [[1 3]
#  [7 9]]

# -----------------------------------------------
# Modifying Elements: Change a single value
# Change the value at (0,0) from 1 to 10
array2d[0, 0] = 10
print("Modified array after changing (0,0) to 10:\n", array2d)
# Expected:
# [[10  2  3]
#  [ 4  5  6]
#  [ 7  8  9]]

# -----------------------------------------------
# Modifying an Entire Row
# Replace second row with new values [11, 12, 13]
array2d[1, :] = [11, 12, 13]
print("Modified array after changing second row:\n", array2d)
# Expected:
# [[10  2  3]
#  [11 12 13]
#  [ 7  8  9]]

# -----------------------------------------------
# Modifying an Entire Column
# Replace third column with new values [14, 15, 16]
array2d[:, 2] = [14, 15, 16]
print("Modified array after changing third column:\n", array2d)
# Expected:
# [[10  2 14]
#  [11 12 15]
#  [ 7  8 16]]
