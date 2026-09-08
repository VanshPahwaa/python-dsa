def solver(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == ".":
                for i in range(1, 10):
                    if isvalid(board, row, col, i):
                        board[row][col] = f"{i}"
                        if solver(board) == True:
                            return True
                        else:
                            board[row][col] = "."
                return False
    return True


def isvalid(board, row, col, num):
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
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
solver(board)
for row in board:
    print(row)
