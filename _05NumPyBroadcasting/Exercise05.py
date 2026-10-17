import numpy as np

array = np.array(list(map(int, input().split())))

array = array.reshape((2,3,4))
array[array > 12] = 0

print(array)

"""
Output:
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    [[[ 1  2  3  4]
    [ 5  6  7  8]
    [ 9 10 11 12]]

    [[ 0  0  0  0]
    [ 0  0  0  0]
    [ 0  0  0  0]]]
"""