import numpy as np

# ---------------------------
# 1. CREATING ARRAYS
# ---------------------------

# From a Python list
array1 = np.array([1, 2, 3, 4, 5])
print("From list:", array1)

# Zeros array (default float64)
zeros = np.zeros((2, 3))
print("Zeros array (2x3):\n", zeros)

# Ones array (integer type)
ones = np.ones((2, 3), dtype=int)
print("Ones array (2x3):\n", ones)

# Full array with a constant value
full_array = np.full((2, 2), fill_value=7)
print("Full array:\n", full_array)

# Identity matrix
identity = np.eye(3)
print("Identity matrix:\n", identity)

# Diagonal matrix
diag = np.diag([1, 2, 3])
print("Diagonal matrix:\n", diag)

# Random array (uniform distribution)
rand_uniform = np.random.rand(2, 3)
print("Random uniform:\n", rand_uniform)

# Random integers
rand_int = np.random.randint(10, 100, size=(2, 2))
print("Random integers:\n", rand_int)

# ---------------------------
# 2. ARRAY SHAPES & RESHAPING
# ---------------------------

# Shape of an array
print("Shape of array1:", array1.shape)

# Reshape a 1D array to 2D
reshaped = array1.reshape(1, 5)
print("Reshaped to 1x5:\n", reshaped)

# Flatten (convert 2D to 1D)
flattened = reshaped.flatten()
print("Flattened:\n", flattened)

# ---------------------------
# 3. ARRAY INDEXING & SLICING
# ---------------------------

array2 = np.array([[10, 20, 30], [40, 50, 60]])

# Access individual element
print("Element at [1, 2]:", array2[1, 2])

# Slice rows and columns
print("First row:", array2[0])
print("Second column:", array2[:, 1])

# Boolean indexing
print("Elements > 25:\n", array2[array2 > 25])

# ---------------------------
# 4. BROADCASTING & OPERATIONS
# ---------------------------

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Element-wise operations
print("Addition:", a + b)
print("Multiplication:", a * b)

# Scalar operations
print("a * 2:", a * 2)

# Broadcasting example
matrix = np.ones((2, 3))
vector = np.array([1, 2, 3])
print("Matrix + Vector:\n", matrix + vector)

# ---------------------------
# 5. AGGREGATION FUNCTIONS
# ---------------------------

print("Sum:", b.sum())
print("Max:", b.max())
print("Mean:", b.mean())
print("Std Dev:", b.std())
print("Argmax:", b.argmax())  # Index of maximum value

# ---------------------------
# 6. DATA TYPES & TYPE CASTING
# ---------------------------

print("Data type of a:", a.dtype)
float_array = a.astype(float)
print("Converted to float:", float_array)

# ---------------------------
# 7. SAVING & LOADING ARRAYS
# ---------------------------

# Save to .npy file
np.save("array_saved.npy", a)
print("Array saved to 'array_saved.npy'")

# Load from .npy file
loaded_array = np.load("array_saved.npy")
print("Loaded array:", loaded_array)

# ---------------------------
# 8. HANDLING NaN & INF
# ---------------------------

nan_array = np.array([1, np.nan, 3, np.inf])

print("Is NaN:", np.isnan(nan_array))
print("Is Inf:", np.isinf(nan_array))
print("Sum ignoring NaN:", np.nansum(nan_array))

# ---------------------------
# 9. RANDOM SEEDING
# ---------------------------

np.random.seed(42)
print("Seeded random array:", np.random.randint(0, 10, size=3))












import numpy as np

# ----------------------------------------------
# SHAPE AND RESHAPING
# ----------------------------------------------
# Every NumPy array has a "shape" – a tuple that tells you its dimensions.
# For example, a 2x3 matrix will have shape (2, 3)

arr = np.array([[1, 2, 3], [4, 5, 6]])  # 2 rows, 3 columns
print("Shape:", arr.shape)  # Output: (2, 3)

# Reshape lets you change the shape of the array without changing its data
reshaped = arr.reshape(3, 2)  # From 2x3 to 3x2
print("Reshaped to 3x2:\n", reshaped)

# Flattening: convert multi-dimensional array to 1D
flattened = arr.flatten()
print("Flattened array:", flattened)

# ----------------------------------------------
# 🧠 SIZE AND MEMORY
# ----------------------------------------------
# .size → total number of elements
# .itemsize → size in bytes of each element
# .nbytes → total bytes consumed

print("Size (total elements):", arr.size)        # 6 elements
print("Item size (bytes):", arr.itemsize)        # e.g., 8 bytes for int64
print("Total memory used (bytes):", arr.nbytes)  # size * itemsize

# ----------------------------------------------
# BROADCASTING
# ----------------------------------------------
# Broadcasting allows NumPy to perform element-wise operations on arrays
# of different shapes (if dimensions are compatible)

matrix = np.array([[1, 2, 3], [4, 5, 6]])   # Shape: (2, 3)
vector = np.array([10, 20, 30])            # Shape: (3,)

# NumPy "broadcasts" the vector to shape (2, 3) to match the matrix
result = matrix + vector
print("Broadcasted addition:\n", result)

# Works only when dimensions are aligned or one is 1
# For example, (3, 1) and (1, 3) → (3, 3)

# ----------------------------------------------
# HANDLING NaN (Not a Number)
# ----------------------------------------------
# np.nan represents undefined or missing values (e.g., 0/0)

nan_array = np.array([1.0, np.nan, 3.0])
print("Original with NaN:", nan_array)

# Check for NaN values
print("Is NaN:", np.isnan(nan_array))  # Returns boolean array

# Sum ignoring NaN values
print("Sum ignoring NaN:", np.nansum(nan_array))

# ----------------------------------------------
# HANDLING Inf (Infinity)
# ----------------------------------------------
# np.inf represents infinity (positive or negative)

inf_array = np.array([1.0, np.inf, -np.inf, 2.0])
print("Original with Inf:", inf_array)

# Check for infinity
print("Is Inf:", np.isinf(inf_array))      # True for inf/-inf
print("Is Finite:", np.isfinite(inf_array))  # False for inf/-inf

# ----------------------------------------------
# BONUS: Shape Validation
# ----------------------------------------------
# While reshaping, ensure that the total number of elements matches
# Otherwise, it will raise a ValueError

a = np.array([1, 2, 3, 4, 5, 6])
try:
    invalid_reshape = a.reshape(2, 4)  # 6 elements cannot reshape into 2x4
except ValueError as e:
    print("Reshape error:", e)

