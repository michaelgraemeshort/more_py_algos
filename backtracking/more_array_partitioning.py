from itertools import combinations
from random import randint


def partition(arr):

    def combination_generator(l, maximum):
        for i in range(1, len(l) + 1):
            for combination in combinations(l, i):
                if sum(combination) <= maximum:
                    yield combination

    target = sum(arr) // 2
    comb_gen = combination_generator(arr, target)
    best = []

    while True:
        try:
            combination = next(comb_gen)
            if sum(combination) == target:
                best = list(combination)
                break
            elif abs(target - sum(combination)) < abs(target - sum(best)):
                best = list(combination)
        except StopIteration:
            break

    for n in best:
        arr.remove(n)

    return best, arr


l = [randint(-10, 10) for i in range(20)]
result = partition(l)
print(f"{result=}")
print(f"{sum(result[0])=}")
print(f"{sum(result[1])=}")
