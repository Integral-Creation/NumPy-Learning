import numpy as np 

val = map(int, input().split())

lis = []
for i in val:
    lis.append(i)

arr = np.array(lis)

k = int(input())

print(f"Elements > {k}: {arr[arr > k]}")
"""
Output:

    10 15 20 25 30
    20
    Elements > 20: [25 30]
"""