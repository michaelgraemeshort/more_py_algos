# how does this work again?
# start at 0
# swap with 1 if necessary
# then with 2
# keep going as far as necessary
# WRONG
# you iterate through the whole array every time
# "keep going as far as necessary" is some other algorithm that I have forgotten
# must revise
# anyway, bubble sort

from random import randint


test_list = [randint(0, 10) for i in range(10)]


def bubble_sort(l):
    swapping = True
    while swapping:
        swapping = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                swapping = True
                l[i], l[i + 1] = l[i + 1], l[i]


print(test_list)
bubble_sort(test_list)
print(test_list)
