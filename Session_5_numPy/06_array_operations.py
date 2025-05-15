import numpy as np

# ----------------------------------------------
# 🎯 GOAL:
# Understand and demonstrate basic and advanced array operations
# ----------------------------------------------

# Creating two sample 1D arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

# 🔹 Element-wise Addition
# Each element of array1 is added to the corresponding element in array2
addition = array1 + array2
print("Addition:", addition)  # [6 6 6 6 6]

# 🔹 Element-wise Subtraction
subtraction = array1 - array2
print("Subtraction:", subtraction)  # [-4 -2  0  2  4]

# 🔹 Element-wise Multiplication
multiplication = array1 * array2
print("Multiplication:", multiplication)  # [5 8 9 8 5]

# 🔹 Element-wise Division
division = array1 / array2
print("Division:", division)  # [0.2 0.5 1.0 2.0 5.0]

# 🔹 Scalar Addition (Broadcasting)
# NumPy automatically applies the scalar to each element
scalar_addition = array1 + 10
print("Scalar Addition:", scalar_addition)  # [11 12 13 14 15]

# 🔹 Scalar Multiplication
scalar_multiplication = array1 * 3
print("Scalar Multiplication:", scalar_multiplication)  # [3 6 9 12 15]

# 🔹 Element-wise Exponentiation
squared = array1 ** 2
print("Squared:", squared)  # [1 4 9 16 25]

# 🔹 Element-wise Square Root
sqrt_array = np.sqrt(array1)
print("Square Root:", sqrt_array)  # [1.         1.41421356 1.73205081 2.         2.23606798]

# 🔹 Modulo Operation
mod_result = array1 % 2
print("Modulo 2 (Odd/Even Check):", mod_result)  # [1 0 1 0 1]

# 🔹 Relational Operations (Boolean Arrays)
greater_than_3 = array1 > 3
print("Greater than 3 (Boolean):", greater_than_3)  # [False False False  True  True]

# 🔹 Boolean Indexing (Filtering)
filtered = array1[array1 > 3]
print("Filtered Elements > 3:", filtered)  # [4 5]

# ----------------------------------------------
# 🔢 AGGREGATION OPERATIONS
# ----------------------------------------------

# Sum of all elements
total_sum = np.sum(array1)
print("Sum:", total_sum)  # 15

# Product of all elements
product = np.prod(array1)
print("Product:", product)  # 120

# Cumulative sum (running total)
cumulative_sum = np.cumsum(array1)
print("Cumulative Sum:", cumulative_sum)  # [1 3 6 10 15]

# Mean of elements
mean_value = np.mean(array1)
print("Mean:", mean_value)  # 3.0

# Median of elements
median_value = np.median(array1)
print("Median:", median_value)  # 3.0

# Standard Deviation
std_deviation = np.std(array1)
print("Standard Deviation:", std_deviation)  # 1.414...

# Variance
variance = np.var(array1)
print("Variance:", variance)  # 2.0

# Min and Max
print("Minimum:", np.min(array1))  # 1
print("Maximum:", np.max(array1))  # 5

# Index of max and min
print("Index of Min:", np.argmin(array1))  # 0
print("Index of Max:", np.argmax(array1))  # 4

# ----------------------------------------------
# 🔄 DOT PRODUCT
# ----------------------------------------------
# Dot product: a1[0]*a2[0] + a1[1]*a2[1] + ... + a1[n]*a2[n]
dot_product = np.dot(array1, array2)
print("Dot Product:", dot_product)  # 35

# ----------------------------------------------
# 🔄 RESHAPING AND TRANSFORMING
# ----------------------------------------------

# Generate an array of 6 elements
example_array = np.arange(1, 7)  # [1 2 3 4 5 6]

# Reshape into 2x3 matrix
reshaped_array = example_array.reshape((2, 3))
print("Reshaped to 2x3:\n", reshaped_array)

# Transpose (swap rows and columns)
transposed = reshaped_array.T
print("Transposed (3x2):\n", transposed)

# Flattening (2D → 1D)
flattened = reshaped_array.flatten()
print("Flattened Array:", flattened)

# ----------------------------------------------
# 🧠 BROADCASTING DEMO (Array + Row Vector)
# ----------------------------------------------

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
row_vector = np.array([10, 20, 30])

# Add row vector to each row (broadcasting)
broadcasted_sum = matrix + row_vector
print("Broadcasted Sum (Matrix + Row Vector):\n", broadcasted_sum)

# ----------------------------------------------
# SUMMARY
# ----------------------------------------------
# Element-wise arithmetic: + - * / ** %
# Scalar operations: Applied to each element (broadcasting)
# Boolean indexing: Filter using conditions
# Aggregation: sum(), prod(), mean(), std(), var(), min(), max()
# Dot product: np.dot(a, b)
# Reshape: .reshape(), .flatten(), .T (transpose)
# Broadcasting: Works when shapes align or are expandable

