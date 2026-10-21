import numpy as np

n, m = map(int, input().split())

# write your code here...
lis = []
for i in range(n):
    val = map(float, input().split())
    temp = []
    for j in val:
        temp.append(j)
    lis.append(temp)

arr = np.array(lis)

mean = np.mean(arr)
std = np.std(arr)

normalized = (arr - mean) / std

print("Original Array:")
print(arr)

print("Mean", mean)
print("Standard Deviation", std)

print("Normalized Array")
print(normalized)


"""
Output:
    2 3
    1 2 3
    4 5 6
    Original Array:
    [[1. 2. 3.]
    [4. 5. 6.]]
    Mean 3.5
    Standard Deviation 1.707825127659933
    Normalized Array
    [[-1.46385011 -0.87831007 -0.29277002]
    [ 0.29277002  0.87831007  1.46385011]]
"""