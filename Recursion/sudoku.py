def isValid(board,row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3] == num:
            return False
    return True
        
def solve_sudoku(sudoku_board):
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j] == None:
                for num in range(1, 10):
                    if isValid(sudoku_board, i, j, num):
                        sudoku_board[i][j] = num

                        if solve_sudoku(sudoku_board):
                            return True
                        else:
                            sudoku_board[i][j] = None
                return False
    return True

def main():
    sudoku_board = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None],
    [None, 9, 8, None, None, None, None, 6, None],
    [8, None, None, None, 6, None, None, None, 3],
    [4, None, None, 8, None, 3, None, None, 1],
    [7, None, None, None, 2, None, None, None, 6],
    [None, 6, None, None, None, None, 2, 8, None],
    [None, None, None, 4, 1, 9, None, None, 5],
    [None, None, None,None, 8, None, None, 7, 9],
]
    solve_sudoku(sudoku_board)
    print(sudoku_board)

main()
    