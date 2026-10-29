import numpy as np 

"""
    Splitting an Arrays
"""

arr = np.array([1,2,3,4,5,6])

parts = np.split(arr, 3)

print(parts)
"""
Output:
    [array([1, 2]), array([3, 4]), array([5, 6])]
"""