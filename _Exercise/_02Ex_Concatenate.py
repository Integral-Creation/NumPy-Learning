import numpy as np

"""
    Concatenating two arrays
"""

arr1 = np.array([
    [1,2,3],
    [4,5,6]
])

arr2 = np.array([
    [5,6,7]
])

combined = np.concatenate((arr1, arr2), axis=0)
print(combined)

"""
Output:
    [[1 2 3]
    [4 5 6]
    [5 6 7]]
"""