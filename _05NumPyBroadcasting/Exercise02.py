import numpy as np

scalar = int(input('Scalar value: '))

arr_2d = np.array([[1,2,3],[4,5,6]])
print("Original 2D Array: ")
print(arr_2d)

# Broadcasting a scalar
result = arr_2d + scalar
print("After adding scalar: ")
print(result)

print("-"*50)

arr_1d = np.array([10,20,30])
print("1D Array: ")
print(arr_1d)

# Broadcasting a 1D array to a 2D array
result_1d_2d = arr_1d + arr_2d
print("After adding 1d array to a 2D array:")
print(result_1d_2d)

print("-"*50)

arr_3d = np.array([[1],[2],[3]])
print("3x1 Matrix:")
print(arr_3d)

result_high_dim = arr_3d + arr_1d
print("After adding 3x1 matrix to 1D array")
print(result_high_dim)

"""
Output:
    Scalar value: 10
    Original 2D Array: 
    [[1 2 3]
    [4 5 6]]
    After adding scalar: 
    [[11 12 13]
    [14 15 16]]
    --------------------------------------------------
    1D Array: 
    [10 20 30]
    After adding 1d array to a 2D array:
    [[11 22 33]
    [14 25 36]]
    --------------------------------------------------
    3x1 Matrix:
    [[1]
    [2]
    [3]]
    After adding 3x1 matrix to 1D array
    [[11 21 31]
    [12 22 32]
    [13 23 33]]
"""