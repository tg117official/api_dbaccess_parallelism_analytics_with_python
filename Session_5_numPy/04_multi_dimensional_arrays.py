import numpy as np

# ---------------------------------------------
# WHAT IS A MULTIDIMENSIONAL ARRAY?
# ---------------------------------------------
# A NumPy array (`ndarray`) can have one or more dimensions.
# - 1D array: A simple list of values (vector)
# - 2D array: A matrix (rows and columns)
# - 3D array: A tensor (stack of matrices, like an image with RGB channels)
# - ND array: Higher dimensional data (e.g., time series of images)

# NumPy represents each dimension with an axis:
# - Axis 0: Rows (first dimension)
# - Axis 1: Columns (second dimension)
# - Axis 2: Depth / Channel (third dimension)
# and so on...

# ---------------------------------------------
# 1D ARRAY (VECTOR)
# ---------------------------------------------
# Shape: (n,) — only one dimension (axis 0)

vector = np.array([10, 20, 30])
# This is a row vector by default.
print("1D array:", vector)
print("Shape:", vector.shape)  # (3,)
print("Number of dimensions:", vector.ndim)  # 1

# ---------------------------------------------
# 2D ARRAY (MATRIX)
# ---------------------------------------------
# Shape: (rows, columns) = (m, n)
# Axis 0: row-wise
# Axis 1: column-wise

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:\n", matrix)
print("Shape:", matrix.shape)  # (2, 3)
print("Number of dimensions:", matrix.ndim)  # 2
print("Element at row 1, col 2:", matrix[1, 2])  # 6

# ---------------------------------------------
# 3D ARRAY (TENSOR)
# ---------------------------------------------
# Shape: (layers, rows, columns) = (l, m, n)
# Can represent color images, video frames, etc.

tensor = np.array([
    [[1, 2], [3, 4]],    # Layer 0
    [[5, 6], [7, 8]]     # Layer 1
])
print("\n3D array:\n", tensor)
print("Shape:", tensor.shape)  # (2, 2, 2)
print("Number of dimensions:", tensor.ndim)  # 3
print("Access tensor[1, 0, 1]:", tensor[1, 0, 1])  # 6

# ---------------------------------------------
# SHAPE AND RESHAPING
# ---------------------------------------------
# .shape returns a tuple that tells you the number of elements in each dimension

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)  # Convert from (6,) to (2, 3)
print("\nReshaped array:\n", reshaped)
print("Shape:", reshaped.shape)

# The number of elements must stay the same when reshaping
# 6 elements in (2, 3) = 2 * 3

# ---------------------------------------------
# FLATTENING
# ---------------------------------------------
# Converts any n-dimensional array to 1D

flattened = reshaped.flatten()
print("Flattened back to 1D:", flattened)

# ---------------------------------------------
# INDEXING AND SLICING
# ---------------------------------------------
# Accessing values in multi-dimensional arrays:
# array[row][col] or array[row, col] for 2D
# array[layer, row, col] for 3D

# Slice first two rows and first two columns
sliced = reshaped[:2, :2]
print("\nSliced subarray:\n", sliced)

# ---------------------------------------------
# BROADCASTING
# ---------------------------------------------
# Broadcasting allows NumPy to apply arithmetic operations between arrays
# of different shapes, as long as they follow broadcasting rules.

a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])           # Shape: (3,)

# b is broadcasted to (2, 3)
broadcasted_sum = a + b
print("\nBroadcasted Addition:\n", broadcasted_sum)

# ---------------------------------------------
# INVALID SHAPE OPERATIONS
# ---------------------------------------------
# You cannot reshape an array if the number of elements doesn't match.

try:
    bad_reshape = arr.reshape(3, 3)  # 6 elements cannot become 3x3
except ValueError as e:
    print("Reshape error:", e)

# ---------------------------------------------
# REAL-WORLD CONTEXT
# ---------------------------------------------
# Use cases of multidimensional arrays:
# - 1D: Sensor readings, feature vectors
# - 2D: Tables, grayscale images, matrices
# - 3D: Color images (H x W x RGB), time-series of tables
# - 4D: Batches of images for deep learning models (N x H x W x C)

# ---------------------------------------------
# SUMMARY
# ---------------------------------------------
# - Use `.ndim` to get number of dimensions
# - Use `.shape` to get size in each dimension
# - Reshape with `.reshape()` keeping total elements the same
# - Use slicing/indexing to extract sub-arrays
# - NumPy uses broadcasting to operate on arrays of different shapes







import numpy as np

# ---------------------------------------------
# 1D ARRAY (VECTOR)
# ---------------------------------------------
# A 1D array is like a single row of numbers — it has only one axis.
vector = np.array([1, 2, 3])
print("1D Array (Vector):")
print(vector)
print("Shape:", vector.shape)  # (3,)
print("Number of dimensions:", vector.ndim)  # 1
print("Data type:", vector.dtype)

# ---------------------------------------------
# 2D ARRAY (MATRIX)
# ---------------------------------------------
# A 2D array is like a table with rows and columns — two axes.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array (Matrix):")
print(matrix)
print("Shape:", matrix.shape)  # (2, 3)
print("Number of dimensions:", matrix.ndim)  # 2
print("Element at row 1, col 2:", matrix[1, 2])  # Accessing a specific element

# Transpose of a matrix (rows become columns and vice versa)
print("Transpose of matrix:\n", matrix.T)

# ---------------------------------------------
# 3D ARRAY (TENSOR)
# ---------------------------------------------
# A 3D array can be visualized as a list of matrices (e.g., images, timeseries).
tensor = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array (Tensor):")
print(tensor)
print("Shape:", tensor.shape)      # (2, 2, 2)
print("Number of dimensions:", tensor.ndim)  # 3

# Accessing tensor element at [layer 1][row 0][col 1]
print("tensor[1, 0, 1]:", tensor[1, 0, 1])  # Output: 6

# ---------------------------------------------
# REAL-WORLD EXAMPLE: Social Media vs Stress
# Each row represents a user: [age, daily_hours_on_social_media, stress_score]
# Let's create a 2D dataset of 4 users
user_data = np.array([
    [18, 4.5, 7.2],
    [25, 2.0, 3.0],
    [30, 3.5, 4.5],
    [40, 1.0, 2.0]
])

print("\nUser Social Media Data (age, hours, stress):")
print(user_data)
print("Shape of dataset:", user_data.shape)  # (4, 3)

# Extract all stress scores (column 2)
stress_scores = user_data[:, 2]
print("Stress Scores:", stress_scores)

# Average stress level
avg_stress = np.mean(stress_scores)
print("Average Stress Score:", avg_stress)

# Get users who spend more than 3 hours on social media
heavy_users = user_data[user_data[:, 1] > 3]
print("\nUsers spending > 3 hours on social media:\n", heavy_users)

# Correlation (not statistical, just difference trend for now)
print("\nObservation: Higher daily hours → Higher stress score (can explore with correlation)")

# ---------------------------------------------
# 🧪 Bonus: Create and inspect a 4D array
# ---------------------------------------------
# A 4D array example — 2 batches of 2 matrices of 2x2 shape
array_4d = np.random.randint(1, 10, size=(2, 2, 2, 2))
print("\n4D Array:")
print(array_4d)
print("Shape:", array_4d.shape)
print("Number of dimensions:", array_4d.ndim)

# ---------------------------------------------
# Summary:
# - 1D: Linear sequence of values
# - 2D: Rows and columns (matrix)
# - 3D: Stacked matrices (tensor)
# - 4D: Data with batches (images, sequences)
# ---------------------------------------------
