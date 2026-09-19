import numpy as np

""" Comparison operator"""

score = np.array([91, 85, 78, 99, 100, 87])

# print boolean value if score is greater than 85
print(score >= 85) # [ True  True False  True  True  True]

# if score is less than 80 assign them 0
score[score < 80] = 0
print(score) # [ 91  85   0  99 100  87]