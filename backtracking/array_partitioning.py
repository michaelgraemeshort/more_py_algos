# divide a given array of numbers into two subarrays such that the difference between their sums is as small as possible


def partition(arr):

    def backtrack(left, right, ideal):
        eligibles = [n for n in right if sum(left) + n <= ideal]
        for n in eligibles:
            left.append(n)
            right.remove(n)
            if ideal in (sum(left), sum(right)):
                return left
            left = backtrack(left, right, ideal)
            if ideal in (sum(left), sum(right)):
                return left
            right.append(left.pop())
        return left

    ideal = sum(arr) // 2
    left = []
    right = arr.copy()
    while not left:
        left = backtrack(left.copy(), right.copy(), ideal)
        ideal -= 1      # NOT ideal. track whichever subarray is closest to ideal as you go? 
    for n in left:
        right.remove(n)
    return sorted(left), sorted(right)


test = list(range(10))
print(partition(test))
