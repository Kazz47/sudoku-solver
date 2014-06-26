#!/usr/local/bin/python3

import solver
import random

def getRandomNumber():
    return random.randint(1,9)

def getZeroWeightedNumber():
    if (random.random() >= 0.6):
        return random.randint(1,9)
    else:
        return 0

def makeGrid():
    grid = [([0]*9) for x in range(9)]
    for row in range(9):
        for col in range(9):
            grid[row][col] = getZeroWeightedNumber()
    return grid

if __name__ == "__main__":
    validGrids = 0
    solvedGrids = 0
    for i in range(100000):
        grid = makeGrid()
        #solver.printGrid(grid)
        if (solver.validGrid(grid)):
            validGrids += 1
            if (solver.solveSudoku(grid)):
                solvedGrids += 1
                print("Solved grid:")
                solver.printGrid(grid)
            else:
                print("Could not be solved:")
                solver.printGrid(grid)
    print("There were {0} valid grids and {1} of them were solved.".format(validGrids, solvedGrids))

