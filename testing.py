from random import randint


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

l = list(range(5))

left = l[:len(l) // 2]
right = l[len(l) // 2:]

print(left)
print(right)