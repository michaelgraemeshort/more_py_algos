# iterate through array, swapping each element as far back as necessary
# no, that's insertion sort
# selection sort iterates through the array and finds the smallest element each time

from random import randint


test_list = [randint(0, 10) for i in range(10)]


def selection_sort(l):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]


print(test_list)
selection_sort(test_list)
print(test_list)
