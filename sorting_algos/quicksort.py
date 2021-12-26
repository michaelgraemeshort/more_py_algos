# choose an element (any element) to use as a "pivot"
# split the array into less than/equal to/more than pivot subarrays
# do so recursively until down to individual elements, so that
# when added back together, the elements are in sorted order

from random import randint


def quicksort(l):
    if len(l) < 2:
        return l
    pivot = l[0]
    less = quicksort([i for i in l if i < pivot])
    equal = [i for i in l if i == pivot]
    more = quicksort([i for i in l if i > pivot])
    return less + equal + more


test_list = [randint(0, 9) for i in range(10)]
print(test_list)
print(quicksort(test_list))
