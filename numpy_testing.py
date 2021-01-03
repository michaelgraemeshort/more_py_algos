# numpy testing

import numpy as np

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# just for the exercise:

def traverse_two_d_np_array(a):
    for i in a:
        for j in i:
            print(j)


def linear_search_2d_array(a, target):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == target:
                return f"{target} found at [{i}][{j}]"
    raise ValueError(f"{target} not in array")





