# works but is horrible

def partition(arr):

    def inner(subarr, index, target):
        if index == len(arr):
            subarrs.append(subarr)
            return
        if sum(subarr) + arr[index] > target:
            inner(subarr, index + 1, target)
            return
        inner(subarr, index + 1, target)
        inner(subarr + [arr[index]], index + 1, target)

    subarrs = []
    target = sum(arr) // 2
    inner([], 0, target)
    max_subarr = max(subarrs)
    for i in max_subarr:
        arr.remove(i)
    return max_subarr, arr


l = [5, 4, 3, 2, 1]
print(partition(l))
