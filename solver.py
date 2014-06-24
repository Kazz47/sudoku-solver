#!/usr/local/bin/python3

def getOpenSpot(grid):
    for row in range(9):
        for col in range(9):
            if(grid[row][col] == 0):
                return (row,col)
    return None

def checkInRow(grid, row, num):
    for col in range(9):
        if(grid[row][col] == num):
            return True
    return False

def checkInCol(grid, col, num):
    for row in range(9):
        if(grid[row][col] == num):
            return True
    return False

def checkInBox(grid, startRow, startCol, num):
    for row in range(3):
        for col in range(3):
            if(grid[startRow+row][startCol+col] == num):
                return True
    return False

def checkIsOkay(grid, row, col, val):
    inRow = checkInRow(grid, row, val)
    inCol = checkInCol(grid, row, val)
    inBox = checkInBox(grid, row - row%3, col - col%3, val)
    if(not inRow and not inCol and not inBox):
        return True
    else:
        return False

def solveSudoku(grid):
    nextSpot = getOpenSpot(grid)
    if(nextSpot == None):
        return True

    row = nextSpot[0]
    col = nextSpot[1]
    for digit in range(1,10):
        if(checkIsOkay(grid, row, col, digit)):
            grid[row][col] = digit
            if(solveSudoku(grid)):
                return True
            else:
                grid[row][col] = 0
    return False

