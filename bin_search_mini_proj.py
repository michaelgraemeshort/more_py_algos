# random mini project inspired by LeetCode, hence oddities
# this is useful https://www.guru99.com/timeit-python-examples.html

from timeit import timeit


test_code_1 = """
def searchInsert(l: list, target: int) -> int:
    return _searchInsert(l, target, start=None, end=None)


def _searchInsert(l, target, start, end):
    if start == None and end == None:
        start = 0
        end = len(l)
    elif start == end:
        return start
    middle = (start + end) // 2
    if target == l[middle]:
        return middle
    elif target < l[middle]:
        return _searchInsert(l, target, start, middle)
    else:
        return _searchInsert(l, target, middle + 1, end)


l = list(range(0, 7, 2))    # 0, 2, 4, 6
result = []
for i in range(-1, 8):
    # print(searchInsert(l, i))
    result.append(searchInsert(l, i))
"""


test_code_2 = """
def searchInsert_2(nums: list, target: int) -> int:
    start = 0
    end = len(nums)
    while start < end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            end = middle
        else:
            start = middle + 1
    return start


l = list(range(0, 7, 2))    # 0, 2, 4, 6
result = []
for i in range(-1, 8):
    # print(searchInsert_2(l, i))
    result.append(searchInsert_2(l, i))
"""


print(timeit(test_code_1))
print(timeit(test_code_2))