# break array down until it can be broken down no more
# merge individual elements together in sorted order
# taking advantage of the fact that merging sorted arrays is efficient

from random import randint


def merge_sort(l):
    def merge(left, right):
        i, j = 0, 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            elif left[i] > right[j]:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    if len(l) == 1:
        return l
    left = merge_sort(l[:len(l) // 2])
    right = merge_sort(l[len(l) // 2:])
    merged = merge(left, right)
    return merged


l = [randint(0, 9) for i in range(9)]

print(l)
print(merge_sort(l))