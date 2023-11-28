import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3])

# Convert the 1D array to a column vector using newaxis
column_vector = arr[:, np.newaxis]

print("Original Array:")
print(arr)

print("\nColumn Vector:")
print(column_vector)
