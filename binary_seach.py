li = [0, 1, 2, 3]


def binary_search(li, value, start=None, end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(li)
    if start == end:
        return -1
    middle = (start + end) // 2
    if li[middle] == value:
        return middle
    elif li[middle] > value:
        return binary_search(li, value, start, middle)
    else:
        return binary_search(li, value, middle + 1, end)


for i in range(-1, 5):
    print(binary_search(li, i))
