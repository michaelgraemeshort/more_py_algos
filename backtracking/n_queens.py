# copied. understand, refactor

class NQueens:
    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def print(self):    # ? refactor, use __str__()
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print()

    def is_safe(self, row, column):
        for i in range(self.n):
            if self.chess_table[row][i] == 1:
                return False

        j = column
        for i in range(row, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        j = column
        for i in range(row, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        return True

    def solve(self, column):
        if column == self.n:
            return True

        for row in range(self.n):
            if self.is_safe(row, column):
                self.chess_table[row][column] = 1
                if self.solve(column + 1):
                    return True
                self.chess_table[row][column] = 0

        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print()
        else:
            print("no solution possible")


board = NQueens(4)
board.solve_NQueens()
