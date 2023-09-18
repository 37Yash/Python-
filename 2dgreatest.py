import numpy as np
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
max_value = None

for row in array_2d:
    for element in row:
        if max_value is None or element > max_value:
            max_value = element

print("The largest number in the 2D array is:", max_value)
