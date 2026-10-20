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