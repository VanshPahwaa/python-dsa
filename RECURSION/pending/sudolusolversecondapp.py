# correct but TLE


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveSudokuRec(board, 0, 0)

    def solveSudokuRec(self, mat, row, col):
        if row == 8 and col == 9:
            print(mat)
            return True

        # If last column of the row go to the next row
        if col == 9:
            row += 1
            col = 0

        # If cell is already occupied then move forward
        if mat[row][col] != ".":
            return self.solveSudokuRec(mat, row, col + 1)

        for num in range(1, 10):
            # If it is safe to place num at current position
            if self.isSafe(mat, row, col, num):
                mat[row][col] = f"{num}"
                if self.solveSudokuRec(mat, row, col + 1):
                    return True
                mat[row][col] = "."
        return False

    def isSafe(self,board, row, col, num):
        for i in range(0, 9):
            if board[row][i] == f"{num}":
                return False
            if board[i][col] == f"{num}":
                return False
            boxrow = row // 3 * 3 + int(i / 3)
            boxcol = col // 3 * 3 + int(i % 3)
            if board[boxrow][boxcol] == f"{num}":
                return False
        return True


board = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "9", ".", ".", "1", ".", ".", "3", "."],
    [".", ".", "6", ".", "2", ".", "7", ".", "."],
    [".", ".", ".", "3", ".", "4", ".", ".", "."],
    ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "2", "5", ".", "6", "4", ".", "."],
    [".", "8", ".", ".", ".", ".", ".", "1", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]

obj=Solution()
obj.solveSudoku(board)
print(board)