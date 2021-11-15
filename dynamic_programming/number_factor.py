# find the number of ways to express N as a sum of 1, 3 and 4
# e.g. 4 can be expressed as (4), (1, 3), (3, 1), (1, 1, 1, 1)

# and 5 can be expressed as all of the above, with 1 at the end
# as well as all of the ways to express 2, with 3 at the end
# and all of the ways to express 1, with 4 at the end

# which is to say, number_factor(5) = number_factor(4) + number_factor(2) + number_factor(1)
# or more generally number_factor(n) = number_factor(n - 1) + number_factor(n - 3) + number_factor(n - 4)

# do this recursively, then dynamically - both top-down, and bottom-up

def number_factor_1(n):     # recursive
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    return number_factor_1(n - 1) + number_factor_1(n - 3) + number_factor_1(n - 4)


def number_factor_2(n, memo_dict):     # dynamic, top-down using memoisation
    non_memo_dict = {0: 0, 1: 1, 2: 1, 3: 2, 4: 4}
    if n in non_memo_dict:
        return non_memo_dict[n]
    if n not in memo_dict:
        branch_1 = number_factor_2(n - 1, memo_dict)
        branch_2 = number_factor_2(n - 3, memo_dict)
        branch_3 = number_factor_2(n - 4, memo_dict)
        memo_dict[n] = branch_1 + branch_2 + branch_3
    return memo_dict[n]


def number_factor_3(n):     # dynamic, bottom-up using tabulation
    # (could use a list, here - simpler, more readable, less space-efficient)
    non_memo_dict = {0: 0, 1: 1, 2: 1, 3: 2, 4: 4}
    if n in non_memo_dict:
        return non_memo_dict[n]    
    # if n == 5...
    n_minus_one = 4
    n_minus_two = 2
    n_minus_three = 1
    n_minus_four = 1

    for i in range(n - 5):  # don't run if n == 5
        temp = n_minus_one + n_minus_three + n_minus_four
        n_minus_four = n_minus_three
        n_minus_three = n_minus_two
        n_minus_two = n_minus_one
        n_minus_one = temp

    return n_minus_one + n_minus_three + n_minus_four


# print(number_factor_1(5))

# my_dict = {}
# print(number_factor_2(100, my_dict))

# print(number_factor_3(100))
