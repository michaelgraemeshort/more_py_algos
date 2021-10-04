# given a set of values, each with a weight and a value, determine which items give the maximum value for a given weight limit
# items can be "broken" such that fractional items and corresponding values can be packed
# unlike coin change problem in that items are NOT infinite in quantity
# contrast with 0-1 knapsack problem

# sort items by descending order of value per unit weight
# pack highest value items that do not exceed weight limit

# he's using Item objects so...

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.value_to_weight = value / weight


def fractional_knapsack(items, capacity):
    to_pack = []
    knapsack_weight = 0
    knapsack_value = 0
    # sort by value_to_weight
    items.sort(key=lambda item: item.value_to_weight)
    # add items until knapsack is full
    while items:
        item = items.pop()
        if knapsack_weight + item.weight <= capacity:
            to_pack.append(item.name)
            knapsack_weight += item.weight
            knapsack_value += item.value
        # otherwise break item
        elif knapsack_weight < capacity:
            spare_capacity = capacity - knapsack_weight
            to_pack.append(item.name + " (partial)")
            knapsack_weight += spare_capacity
            knapsack_value += item.value * spare_capacity / item.weight
        else:
            break
    return to_pack, knapsack_weight, knapsack_value



items = [
    Item("1", 1, 2),
    Item("2", 2, 3),
    Item("3", 3, 4),
    Item("4", 4, 5),
    Item("5", 5, 6)
]

print(fractional_knapsack(items, 12))