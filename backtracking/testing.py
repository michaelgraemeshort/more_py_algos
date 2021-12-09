# currently handles non-negative integers only

from random import randint


def partition(arr):

    subarrays = []

    def create_valid_subarrays(subarray, index, maximum):
        if index == len(arr):
            subarrays.append(subarray)
            return
        if sum(subarray) + arr[index] <= maximum:
            create_valid_subarrays(subarray, index + 1, maximum)
            create_valid_subarrays(subarray + [arr[index]], index + 1, maximum)

    target = sum(arr) // 2
    create_valid_subarrays([], 0, target)
    best = max(subarrays, key=lambda x: sum(x))
    for i in best:
        arr.remove(i)
    return best, arr


l = [randint(0, 10) for i in range(20)]
result = partition(l)
print(f"{result=}")
print(f"{sum(result[0])=}")
print(f"{sum(result[1])=}")
