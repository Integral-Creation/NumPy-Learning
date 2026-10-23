import numpy as np

# Initialize an empty list to store the rows
temps_list = []

# Take input for 4 cities (each with 5 days of temperatures)
for i in range(4):
    row = list(map(int, input(f"city {i+1}: ").split()))
    temps_list.append(row)

# Convert the list to a 2D NumPy array
temps_2d = np.array(temps_list)

# Create a mask for temperatures greater than 30°C
mask = temps_2d > 30

# Filter temperatures using the mask
temp_filer = temps_2d[mask]

# Print results
print("Boolean Mask:")
print(mask)
print("Temperatures above 30 C:")
print(temp_filer)
