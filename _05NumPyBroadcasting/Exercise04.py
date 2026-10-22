import numpy as np

marks = np.array([
    [78, 85, 92],
    [65, 70, 75],
    [88, 90, 95],
    [55, 60, 58]
])


student_avg = marks.mean(axis=1)
print("Student Averages:", student_avg)

student_max = marks.max(axis=1)
print("Highest Mark per Student:", student_max)

subject_avg = marks.mean(axis=0)
print("Subject-wise Averages:", subject_avg)

students_above_75 = np.where(student_avg > 75)[0] + 1
print("Students with Average > 75 (1-indexed):", students_above_75)

overall_max = marks.max()
print("Overall Highest Mark:", overall_max)

"""
Output:
    Student Averages: [85.         70.         91.         57.66666667]
    Highest Mark per Student: [92 75 95 60]
    Subject-wise Averages: [71.5  76.25 80.  ]
    Students with Average > 75 (1-indexed): [1 3]
    Overall Highest Mark: 95
"""