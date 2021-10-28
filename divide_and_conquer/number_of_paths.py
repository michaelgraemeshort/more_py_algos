# given a 2D matrix, in which each cell has a given cost of access,
# and in which you can only go right or down one from the current cell,
# find the number of ways to reach the bottom right cell for a given cost


def number_of_paths(matrix, target_cost, current_cost=0, row=0, column=0):
    # start at the start
    # explore all valid paths
    # each time you reach the end with the given cost, return 1
    last = len(matrix) - 1
    current_cell = matrix[row][column]
    current_cost += current_cell
    if current_cost > target_cost:
        # go no further
        return 0
    # if at end:
    if row == last and column == last:
        if current_cost == target_cost:
            return 1
        return 0
    # if at last row, do not attempt to explore next row:
    if row == last:
        return number_of_paths(matrix, target_cost, current_cost, row, column + 1)
    # likewise for last column:
    if column == last:
        return number_of_paths(matrix, target_cost, current_cost, row + 1, column)
    # else
    branch_1 = number_of_paths(matrix, target_cost, current_cost, row + 1, column)
    branch_2 = number_of_paths(matrix, target_cost, current_cost, row, column + 1)
    return branch_1 + branch_2


matrix = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3]
]

print(number_of_paths(matrix, 25))
