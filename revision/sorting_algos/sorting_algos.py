# Bubble Sort: iterate through the whole array, swapping items as appropriate, repeatedly until no swaps occur
# first pass moves biggest element to end of list
# second moves second biggest element to second last
# etc

from random import randint


def bubble_sort(l):
    swapping = True
    while swapping:
        for i in range(len(l) - 1):
            swapping = False
            if l[i] > l[i + 1]:
                swapping = True
                l[i], l[i + 1] = l[i + 1], l[i]


# Selection Sort
# starts at index 0
# compares element at 0 with each other element
# if other element is smaller, swaps elements, thus placing smallest at beginning
# next iteration starts at index 1


def selection_sort(l):
    pass


# Insertion Sort
# start at index 1
# check if element at index 0 is bigger
# swap if so
# move to index 2
# check if element at index 1 is bigger
# swap if so, THEN check if element at index 0 is bigger, and swap if so
# basically, compare each element to the one to its left, swap as many times as necessary until the element to its left is smaller
# much like sorting a deck of cards


def insertion_sort(l):
    pass


def merge_sort(l):
    pass


def quicksort(l):
    pass


def heapsort(l):
    pass


l = [2, 1]
bubble_sort(l)
print(l)

# for i in range(10):
#     test_list = [randint(-9, 9) for i in range(10)]
#     if not bubble_sort(test_list) == test_list.sort():
#         print("broken")
