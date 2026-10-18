import numpy as np

lis = list(map(int, input().split()))
k = int(input())

array = np.array(lis)
np.savetxt('data.csv', array, fmt="%d", delimiter=',')

array_read = np.loadtxt('data.csv', dtype=int, delimiter=',')

filtered = array_read[array_read > k]
print(array_read)
print(filtered)

"""
Output:
    10 20 30 40 50
    25
    [10 20 30 40 50]
    [30 40 50]
"""