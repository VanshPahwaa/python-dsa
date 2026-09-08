def solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for num in range(1, 10):
                    if isvalid(board, row, col, str(num)):
                        board[row][col] = str(num)
                        if solver(board):
                            return True
                        board[row][col] = "."  # backtrack
                return False  # No valid number found → backtrack
    return True  # No empty cells left → board solved

def isvalid(board, row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

# Given Sudoku board with "." as empty cells
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

if solver(board):
    for row in board:
        print(row)
else:
    print("No solution exists.")
