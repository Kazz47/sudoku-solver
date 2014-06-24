#!/usr/local/bin/python3

import boards
import solver

def check_sudoku(grid):
    # Sanity Check
    if(len(grid) != 9):
        return None
    else:
        for row in grid:
            if(len(row) != 9):
                return None
            else:
                for item in row:
                    if(not isinstance(item, int) or item < 0 or item > 9):
                        return None

    # Check correct number of vals in each row, column, and box (skip when we hit a zero)

    found_zero = False

    # Check rows
    for row in range(9):
        bit_list = [False] * 10;
        for col in range(9):
            current_item = grid[row][col]
            if(current_item != 0 and bit_list[current_item]):
                print("{0} was duplicated in row {1}".format(current_item, row))
                return False
            else:
                bit_list[current_item] = True

    # Check columns
    for col in range(9):
        bit_list = [False] * 10;
        for row in range(len(grid)):
            current_item = grid[row][col]
            if(current_item != 0 and bit_list[current_item]):
                print("{0} was duplicated in column {1}".format(current_item, row))
                return False
            else:
                bit_list[current_item] = True

    # Check boxes
    start_positions = [[0,0],
                       [0,3],
                       [0,6],
                       [3,0],
                       [3,3],
                       [3,6],
                       [6,0],
                       [6,3],
                       [6,6]]
    for i in range(9):
        x = start_positions[i][0]
        y = start_positions[i][1]
        bit_list = [False] * 10;
        for row in range(3):
            for col in range(3):
                current_item = grid[y+row][x+col]
                if(current_item != 0 and bit_list[current_item]):
                    print("{0} was duplicated in box ({1},{2})".format(current_item, x//3, y//3))
                    return False
                else:
                    bit_list[current_item] = True

    return solver.solveSudoku(grid)


print(check_sudoku(boards.ill_formed))
print(check_sudoku(boards.ill_formed_2))
print(check_sudoku(boards.valid))
print(check_sudoku(boards.invalid))
print(check_sudoku(boards.invalid_2))
print(check_sudoku(boards.invalid_3))
print(check_sudoku(boards.easy))
print(check_sudoku(boards.hard))

