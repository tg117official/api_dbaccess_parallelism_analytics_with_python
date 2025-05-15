import numpy as np

array2d = np.array([
    [4, 1, 7],
    [2, 5, 8],
    [6, 3, 9]
])

column_sum = np.sum(array2d, axis=1)

print(column_sum)