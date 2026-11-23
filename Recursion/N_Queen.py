def place_n_queends(col, n,ans, board, left_row, upper_diag, lower_diag):
    if col == n:
        ans.append([row.copy() for row in board])
        return
    for row in range(n):
        if left_row[row] is None and upper_diag[col-row+n-1] is None and lower_diag[row+col] is None:
            left_row[row] = 1
            upper_diag[col-row+n-1] = 1
            lower_diag[row+col] = 1
            board[row][col] = 'Q'
            place_n_queends(col+1,  n,ans, board, left_row, upper_diag, lower_diag)
            left_row[row] = None
            upper_diag[col-row+n-1] = None
            lower_diag[row+col] = None
            board[row][col] = None


def main():
    ans = []
    n = 4
    board = [[None for _ in range(n)]for _ in range(n)]
    left_row = [None for _ in range(n)]
    upper_diag = [None for _ in range(2*n-1)]
    lower_diag = [None for _ in range(2*n-1)]
    place_n_queends(0,n, ans, board, left_row, upper_diag, lower_diag)
    print(ans)

main()
