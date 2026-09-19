import numpy as np
""" Element-wise Arithmetic"""
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2) # [5,7,9]
print(array1 - array2) # [-3 -3 -3]
print(array1 * array2) # [ 4 10 18]
print(array1 / array2) # [0.25 0.4  0.5 ]
print(array1 ** array2) # [  1  32 729]