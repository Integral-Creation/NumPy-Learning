import numpy as np

"""
    In NumPy, the random module is used to generate random numbers, create random arrays, select random elements, and shuffle arrays.
"""

rng = np.random.default_rng(seed=1)

print(rng.integers(low= 1, high=101, size=(3,2)))

"""
Output:
    [[48 52]
    [76 96]
    [ 4 15]]
"""
np.random.seed(seed=1)
print(np.random.uniform(low=-1 , high=1, size=(3,3)))

"""
Output:
    [[-0.16595599  0.44064899 -0.99977125]
    [-0.39533485 -0.70648822 -0.81532281]
    [-0.62747958 -0.30887855 -0.20646505]]
"""

fruits = np.array(["apple", "orange", "banana", "coconut"])
fruit = rng.choice(fruits, size=2)

print(fruit)


arr = np.array([1,2,4,5])
np.random.shuffle(arr)
print(arr)