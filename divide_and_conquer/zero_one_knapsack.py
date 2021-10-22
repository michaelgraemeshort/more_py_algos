# like greedy_algos/fractional_knapsack_problem.py, but no item breakage allowed
# naive brute-force recursive approach
# modified power set, again

class Item:  # this seems unnecessary
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def zero_one_knapsack(items, capacity, current_index=0):
    # if capacity <= 0 or current_index < 0 or current_index >= len(items): # why would current_index be < 0
    if capacity <= 0 or current_index >= len(items):
        return 0
    elif items[current_index].weight <= capacity:
        # pack the item
        value_1 = items[current_index].value + zero_one_knapsack(
            items, capacity - items[current_index].weight, current_index + 1)
        # don't pack the item
        value_2 = zero_one_knapsack(items, capacity, current_index + 1)
        return max(value_1, value_2)
    else:
        return 0


items = [Item(31, 3), Item(26, 1), Item(17, 2), Item(72, 5)]
capacity = 7

print(zero_one_knapsack(items, capacity))
