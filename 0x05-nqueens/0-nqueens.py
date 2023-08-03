#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    # Check if a queen can be placed at (row, col)
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False
    return True

def solve_nqueens(n, board, row=0):
    if row == n:
        for row in board:
            print(' '.join(map(str, row)))
        print()
    else:
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_nqueens(n, board, row + 1)
                board[row][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    n_str = sys.argv[1]
    
    if not n_str.isnumeric():
        print("N must be a number")
        sys.exit(1)
    
    n = int(n_str)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(n, board)

if __name__ == "__main__":
    main()

