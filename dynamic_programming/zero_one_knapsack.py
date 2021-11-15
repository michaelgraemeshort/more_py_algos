# the problem with the naive recursive approach is that it creates overlapping subproblems
# so cache the results of those subproblems
# (e.g. zero_one_knapsack(capacity = 1, index = 1) might get called repeatedly)


class Item:  # this seems unnecessary
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def zero_one_knapsack(items, memo_dict, capacity, index=0):
    # if no items remaining:
    if index == len(items):
        return 0
    item = items[index]
    # if item doesn't fit, move on to the next:
    if item.weight > capacity:
        return zero_one_knapsack(items, memo_dict, capacity, index + 1)
    # otherwise, check memo_dict for the solution:
    key = str(capacity) + str(index)
    if key not in memo_dict:
        # add it
        pack = item.value + zero_one_knapsack(items, memo_dict, capacity - item.weight, index + 1)
        dont_pack = zero_one_knapsack(items, memo_dict, capacity, index + 1)
        memo_dict[key] = max(pack, dont_pack)
    return memo_dict[key]


items = [Item(31, 3), Item(26, 1), Item(17, 2), Item(72, 5)]
memo_dict = {}
capacity = 7

print(zero_one_knapsack(items, memo_dict, capacity))
