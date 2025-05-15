import numpy as np

# ---------------------------------------------
# 🎯 GOAL:
# Learn all foundational operations and concepts on a 4D array
# 4D shape convention (N, C, H, W) — often used in DL for images
# Example: 2 batches, 3 channels, 4 rows, 5 columns
# Shape: (2, 3, 4, 5)
# ---------------------------------------------

# Create a 4D array of random integers between 1 and 100
arr_4d = np.random.randint(1, 100, size=(2, 3, 4, 5))

# ---------------------------------------------
# 🔍 BASICS OF 4D ARRAY
# ---------------------------------------------

print("🔷 4D Array (Shape: 2 batches, 3 channels, 4x5 image):\n", arr_4d)

# .shape gives the size of each dimension
print("\nShape:", arr_4d.shape)  # (2, 3, 4, 5)

# .ndim gives the number of dimensions
print("Number of Dimensions (ndim):", arr_4d.ndim)  # 4

# .size gives the total number of elements
print("Total Elements (size):", arr_4d.size)  # 2*3*4*5 = 120

# .itemsize gives memory used by one element (in bytes)
print("Item Size (bytes):", arr_4d.itemsize)

# .nbytes gives total memory usage
print("Total Bytes (nbytes):", arr_4d.nbytes)

# ---------------------------------------------
# 🧩 INDEXING EXAMPLES (Manual Traversal)
# ---------------------------------------------

# Access 1st batch, 2nd channel, 3rd row, 4th column
print("\nSingle Element (arr_4d[0, 1, 2, 3]):", arr_4d[0, 1, 2, 3])

# Access full 1st batch
print("\n1st Batch (arr_4d[0]):\n", arr_4d[0])

# Access full 2nd channel of the 2nd batch
print("\n2nd Batch, 2nd Channel (arr_4d[1, 1]):\n", arr_4d[1, 1])

# Access all batches, 1st channel (slices across batches)
print("\nAll Batches, 1st Channel:\n", arr_4d[:, 0])

# Access all rows in 1st batch, 2nd channel, and first column only
print("\nAll Rows, 1st Column of 2nd Channel in 1st Batch:\n", arr_4d[0, 1, :, 0])

# ---------------------------------------------
# 🔪 SLICING AND SUBSETTING
# ---------------------------------------------

# Slice: first batch, all channels, first two rows, all columns
sliced = arr_4d[0, :, :2, :]
print("\nSliced [0, :, :2, :]:\n", sliced)

# Slice: all batches, only 2nd channel, last two rows, last 3 columns
subset = arr_4d[:, 1, 2:, 2:]
print("\nSliced [:, 1, 2:, 2:]:\n", subset)

# ---------------------------------------------
# 🔁 RESHAPING AND FLATTENING
# ---------------------------------------------

# Flatten entire 4D array to 1D
flattened = arr_4d.flatten()
print("\nFlattened Array (1D):", flattened)
print("Flattened Shape:", flattened.shape)

# Reshape 4D to 2D: (2 batches * 3 channels = 6, each image is 4x5 = 20)
reshaped = arr_4d.reshape(6, 20)
print("\nReshaped to (6, 20):\n", reshaped)

# ---------------------------------------------
# 📌 BROADCASTING INSIGHT (simplified 2D case)
# ---------------------------------------------

# Broadcasting demo (small scale for simplicity)
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])           # Shape: (3,)
print("\nBroadcasting Example (a + b):\n", a + b)
# NumPy stretches b to match a's shape for element-wise operation

# ---------------------------------------------
# 📊 REAL-WORLD USE CASES OF 4D ARRAYS
# ---------------------------------------------
# - Computer Vision: 4D arrays represent batches of color images
#   Shape: (batch_size, channels, height, width)
# - Medical Imaging: 4D MRI/CT scans
# - NLP: Batch of word embeddings over sequences
# - Deep Learning: Input data format for CNNs

# ---------------------------------------------
# SUMMARY OF CONCEPTS
# ---------------------------------------------
# ndim        → Number of dimensions
# shape       → Tuple of dimensions
# size        → Total number of elements
# itemsize    → Memory used per element
# nbytes      → Total memory usage
# Indexing    → Access any level using [i,j,k,l]
# Slicing     → Use colons `:` to subset axes
# Flattening  → .flatten() for 1D vector
# Reshaping   → .reshape(new_shape) while preserving total elements
# Broadcasting→ Smaller arrays auto-expanded for operations (if compatible)
