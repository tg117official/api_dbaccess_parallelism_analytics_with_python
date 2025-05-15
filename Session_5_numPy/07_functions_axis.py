import numpy as np

# ----------------------------------------------
# Create a 3x3 NumPy 2D array
# Each sub-array represents a row
array2d = np.array([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
])

# ----------------------------------------------
# 🔢 Basic Aggregation Functions (All Elements)
# ----------------------------------------------

# Sum of all elements in the array
total_sum = np.sum(array2d)
print("Total sum of all elements:", total_sum)  # Output: 45

# Mean (average) of all elements
mean_value = np.mean(array2d)
print("Mean of all elements:", mean_value)  # Output: 5.0

# Maximum value in the entire array
max_value = np.max(array2d)
print("Maximum value:", max_value)  # Output: 9

# Minimum value in the entire array
min_value = np.min(array2d)
print("Minimum value:", min_value)  # Output: 1

# ----------------------------------------------
# 🔍 Element-wise Mathematical Operation
# ----------------------------------------------

# Square root of each element in the array
sqrt_values = np.sqrt(array2d)
print("Square root of each element:\n", sqrt_values)
# Output is a 2D array with the square root of each value

# ----------------------------------------------
# 🔁 Sorting
# ----------------------------------------------

# Sort elements in each row (axis=1)
# Sorting is done row-wise by default when axis=1
sorted_array = np.sort(array2d, axis=1)
print("Elements sorted in each row:\n", sorted_array)

# ----------------------------------------------
# 🧮 Aggregations Using Axis Parameter
# ----------------------------------------------

# Sum of elements in each column (axis=0)
# axis=0 means operate **down the columns**
column_sum = np.sum(array2d, axis=0)
print("Sum along each column:", column_sum)  # Output: [6 15 24]

# Mean of elements in each row (axis=1)
# axis=1 means operate **across the rows**
row_mean = np.mean(array2d, axis=1)
print("Mean along each row:", row_mean)  # Output: [4. 5. 6.]

# Maximum value in each row (axis=1)
row_max = np.max(array2d, axis=1)
print("Max value in each row:", row_max)  # Output: [7 8 9]

# Minimum value in each column (axis=0)
column_min = np.min(array2d, axis=0)
print("Min value in each column:", column_min)  # Output: [1 4 7]

# ----------------------------------------------
# 📌 Explanation of Axis Parameter
# ----------------------------------------------
# axis=0 → Operates **column-wise** (down the rows)
#          Think: "reduce rows, keep columns"
# axis=1 → Operates **row-wise** (across the columns)
#          Think: "reduce columns, keep rows"

# Example shape (3, 3):
# axis=0 collapses the rows → result is (3,)
# axis=1 collapses the columns → result is (3,)

# Summary:
# Use axis=0 when you want to analyze/aggregate per **column**
# Use axis=1 when you want to analyze/aggregate per **row**
