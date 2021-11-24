# alternative non-backtracking approach
# modified power set
# broken, perhaps fix later


def partition(right):

    def inner(left, index, target):
        if index == len(right):
            return []
        dont_add = left + inner(left, index + 1, target)
        if sum(left) + right[index] <= target:
            left.append(right[index])
            add = left + inner(left, index + 1, target)
            return max(dont_add, add)
        return dont_add

    target = sum(right) // 2
    return inner([], 0, target)


l = [9, 9, 3]

print(partition(l))
