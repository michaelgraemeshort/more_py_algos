# like sorting a deck of cards
# shuffle cards from the unsorted portion back into the sorted portion

from random import randint


test_list = [randint(0, 10) for i in range(10)]


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break


print(test_list)
insertion_sort(test_list)
print(test_list)
