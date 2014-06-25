#!/usr/local/bin/python3

import boards
import solver

def check_sudoku(grid):
    if (solver.validGrid(grid)):
        if (solver.solveSudoku(grid)):
            return solver.validGrid(grid)
    else:
        return False

print(check_sudoku(boards.ill_formed))
print(check_sudoku(boards.ill_formed_2))
print(check_sudoku(boards.valid))
print(check_sudoku(boards.invalid))
print(check_sudoku(boards.invalid_2))
print(check_sudoku(boards.invalid_3))
print(check_sudoku(boards.easy))
print(check_sudoku(boards.hard))

