from random import randint
from math import sqrt, ceil


test_list = [randint(-10, 10) for i in range(10)]


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break


def bucket_sort(l):
    # how many buckets?
    # course suggests square root of number of elements in list
    number_of_buckets = ceil(sqrt(len(l)))
    buckets = [[] for i in range(number_of_buckets)]
    largest = max(l)
    smallest = min(l)
    spread = largest - smallest
    for value in l:
        index = ceil((value - smallest) / spread * number_of_buckets) - 1
        if index == -1:  # edge case in this implementation
            buckets[0].append(value)
        else:
            buckets[index].append(value)
    for bucket in buckets:
        insertion_sort(bucket)
    i = 0
    for j in range(number_of_buckets):
        for k in range(len(buckets[j])):
            l[i] = buckets[j][k]
            i += 1
    # more readable, less space-efficient:
    # sorted_l = []
    # for bucket in buckets:
    #     insertion_sort(bucket)
    #     sorted_l.extend(bucket)
    # return sorted_l


print(test_list)
# test_list = bucket_sort(test_list)
bucket_sort(test_list)
print(test_list)
