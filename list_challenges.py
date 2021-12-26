# find the missing number in an list of integers
# clue: 1 + 2 + 3 + ... + n = n(n + 1) / 2
# search triangular numbers for background

def find_missing_number(l: list) -> int:
    return l[-1] * (l[-1] + 1) // 2 - sum(l)


# two sum, per leetcode

def two_sum(l: list, n: int) -> list:
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == n:
                return [i, j]


# find maximum possible product of two list items

def max_product_of_two(l: list) -> int:
    highest, second_highest = 0, 0
    for number in l:
        if number > highest:
            second_highest = highest
            highest = number 
        elif number > second_highest:
            second_highest = number 
    return highest * second_highest


# contains duplicate - implement using list (!)

def contains_duplicate(l: list) -> bool:
    unique_values = []
    for i in l:
        if i in unique_values:
            return False
        else:
            unique_values.append(i)
    return True


# rotate 3x3 matrix 90' clockwise
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

def rotate_clockwise(l):
    pass
# surely just a case of creating a new matrix and populating it with nine assignment statements
# or doing the same in-place using some temporary variables
# can be done with logic. pointless for small matrix


def pairSum(myList, n):
    pairs = []
    for i in range(len(myList) - 1):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == n:
                pairs.append(str(myList[i]) + "+" + str(myList[j]))
    return pairs
