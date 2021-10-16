# you are a robber and know how much gold is in each house of a row of houses
# you cannot steal from two adjacent houses
# what is the maximum amount that can be stolen?

# https://medium.com/outco/how-to-solve-the-house-robber-problem-f3535ebaef1b
# two approaches: brute force, dynamic programming

# brute force: try all valid combinations of houses
# modified power set
# for each house:
# 1. steal and skip the next, OR skip
# 2. return to 1


# houses = [3, 1, 5, 1, 6]


def max_loot_recursive(houses):

    def rob_house(index):
        if index >= len(houses):
            return 0
        return max(                                     # which is better?
            houses[index] + rob_house(index + 2),       # steal from this house and skip the next, or
            rob_house(index + 1))                       # skip this house?
                                                        # (tries every valid combination, including lots of junk ones)
    return rob_house(0)                                 # (leading to a not-quite-exponential runtime)


# dynamic: iterate through houses, keep track of maximum possible loot at each stage
# by asking: better to rob this house instead of the previous one, or not?

houses = [5, 1, 1, 5]   # [5, 5, 6, 10]
houses_2 = [1, 2, 3, 4, 5]

def max_loot(houses):   # my effort
    # you always rob the first house so
    loot = [houses[0]]
    # move on to the next
    if houses[1] > houses[0]:
        loot.append(houses[1])
    else:
        loot.append(houses[0])
    # now those are set up
    for i in range(2, len(houses)):
        # if you didn't rob the last house
        if loot[i - 1] == loot[i - 2]:
            # rob this one
            loot.append(loot[i - 2] + houses[i])
        # if the next house has more loot, rob it instead
        elif houses[i] > houses[i - 1]:
            loot.append(loot[i - 2] + houses[i])    # could DRY this up
        # if the next house does not have more loot, skip house, loot remains the same
        else:
            loot.append(loot[i - 1])
    return loot[-1]


def max_loot_2(houses): # translated, constant space. much better. my shitty variable names
    loot = 0
    prev_loot = 0
    for i in range(len(houses)):
        house = houses[i]
        new_loot = max(prev_loot + house, loot)
        prev_loot = loot
        loot = new_loot
    return loot
    # makes use of insight that loot either increases or stays constant
    # come on brain


print(max_loot_2(houses))
