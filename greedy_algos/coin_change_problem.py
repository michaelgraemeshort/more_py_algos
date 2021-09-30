# find the minimum number of coins needed to make up a given amount
# greedy version, not dynamic programming version

denominations = [1, 2, 5, 10, 20, 50, 100, 1000]

# add the largest coin that does not exceed the target amount to the total


def coins_required(amount):
    total = 0
    coins = []
    for denomination in denominations[::-1]:
        while total + denomination <= amount:
            total += denomination
            coins.append(denomination)
    return coins


print(coins_required(2035))
