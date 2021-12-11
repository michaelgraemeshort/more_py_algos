class ChessBoard:
    def __init__(self, n):
        self.matrix = [[0 for i in range(n)] for j in range(n)]

    def __str__(self):
        for row in self.matrix:
            for square in row:
                if square == 0:
                    print(" - ", end="")
                else:
                    print(" Q ", end="")
            print()
        return ""

    def solve(self):
        return self._solve(len(self.matrix), 0)

    def _solve(self, n, column):
        if n == column:
            return self
        for row in range(n):
            if self.is_safe(row, column):
                # place queen. don't forget to undo this and BACKTRACK if necessary
                self.matrix[row][column] = 1
                # move on to next column
                solution = self._solve(n, column + 1)
                if solution:
                    return solution
                # this is the backtracking bit
                self.matrix[row][column] = 0

    def is_safe(self, row, column):
        # check the row to the left
        for i in range(column):
            if self.matrix[row][i] == 1:
                return False
        # check the up-left diagonal
        r = row - 1
        c = column - 1
        for i in range(min(row, column)):
            if self.matrix[r][c] == 1:
                return False
            r -= 1
            c -= 1
        # check the down-left diagonal
        r = row + 1
        c = column - 1
        while r < len(self.matrix) and c >= 0:  # this is nasty, refactor
            if self.matrix[r][c] == 1:
                return False
            r += 1
            c -= 1
        return True


board = ChessBoard(8)
print(board.solve())
