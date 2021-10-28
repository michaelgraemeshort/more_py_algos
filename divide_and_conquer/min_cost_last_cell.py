# given a 2D matrix, in which each cell has a given cost of access,
# and in which you can only go right or down one from the current cell,
# find the minimum cost to reach the bottom right cell

def min_cost(matrix, row=0, column=0):
    current_cell = matrix[row][column]
    # if at bottom right corner
    if row == len(matrix) - 1 and column == len(matrix) - 1:
        return current_cell
    # if at bottom row
    if row == len(matrix) - 1:
        return current_cell + min_cost(matrix, row, column + 1)
    # if at rightmost column
    if column == len(matrix) - 1:
        return current_cell + min_cost(matrix, row + 1, column)
    # else
    branch_1 = min_cost(matrix, row + 1, column)
    branch_2 = min_cost(matrix, row, column + 1)
    return current_cell + min(branch_1, branch_2)


matrix = [
    [1, 2],
    [3, 4]
]

print(min_cost(matrix))

# as a recursive divide and conquer problem
# think about a small matrix first
# e.g.
# [1]
# return 1, obviously
# because row and column arguments are both n - 1 where n is len(side)
# or
# [[1, 2],
#  [3, 4]]
# from 1, go right, OR go down
# basically, go right if possible, call min_cost again
# AND go down if possible, call min_cost again
# compare whichever of the two yields the min cost
