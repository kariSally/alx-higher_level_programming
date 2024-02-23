#!/usr/bin/python3
"""A module to solve the N-Queen problem."""
import sys


def is_valid(grid, i, j):
    """Check if current configuration is valid."""
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]
    for k in range(8):
        ni = i + dx[k]
        nj = j + dy[k]
        while (0 <= ni < len(grid)) and (0 <= nj < len(grid)):
            if grid[ni][nj] == 'Q':
                return False
            ni += dx[k]
            nj += dy[k]
    return True


def solve_nqueen(grid, i=0):
    """Solve the N-Queen problme."""
    if i >= len(grid):
        grid_list = []
        for k, row in enumerate(grid):
            for m, elem in enumerate(row):
                if elem == 'Q':
                    grid_list.append([k, m])
        print(grid_list)
        return

    for j in range(len(grid)):
        grid[i][j] = 'Q'
        if is_valid(grid, i, j):
            solve_nqueen(grid, i+1)
        grid[i][j] = '.'


def main():
    """Enter to the problem from the main function."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    grid = [['.']*n for _ in range(n)]
    solve_nqueen(grid)


if __name__ == "__main__":
    main()
