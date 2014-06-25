#!/usr/local/bin/python3

def printGrid(grid):
    for row in grid:
        print(row)
    print("")

def validFormatting(grid):
    if (type(grid) is not list):
        return False
    elif (len(grid) != 9):
        return False
    else:
        for row in grid:
            if (type(row) is not list):
                return False
            elif (len(row) != 9):
                return False
            else:
                for item in row:
                    if (type(item) is not int or item < 0 or item > 9):
                        return False
    return True

def validRows(grid):
    found_zero = False
    for row in range(9):
        bit_dict = {}
        for col in range(9):
            current_item = grid[row][col]
            if (current_item != 0 and current_item in bit_dict):
                #print("{0} was duplicated in row {1}".format(current_item, row))
                return False
            else:
                bit_dict[current_item] = True
    return True

def validCols(grid):
    found_zero = False
    for col in range(9):
        bit_dict = {}
        for row in range(len(grid)):
            current_item = grid[row][col]
            if (current_item != 0 and current_item in bit_dict):
                #print("{0} was duplicated in column {1}".format(current_item, row))
                return False
            else:
                bit_dict[current_item] = True
    return True

def validBoxes(grid):
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
        bit_dict = {}
        for row in range(3):
            for col in range(3):
                current_item = grid[y+row][x+col]
                if (current_item != 0 and current_item in bit_dict):
                    #print("{0} was duplicated in box ({1},{2})".format(current_item, x//3, y//3))
                    return False
                else:
                    bit_dict[current_item] = True
    return True

def getOpenSpot(grid):
    for row in range(9):
        for col in range(9):
            if (grid[row][col] == 0):
                return (row,col)
    return None

def checkInRow(grid, row, num):
    for col in range(9):
        if (grid[row][col] == num):
            return True
    return False

def checkInCol(grid, col, num):
    for row in range(9):
        if (grid[row][col] == num):
            return True
    return False

def checkInBox(grid, startRow, startCol, num):
    for row in range(3):
        for col in range(3):
            if (grid[startRow+row][startCol+col] == num):
                return True
    return False

def checkIsOkay(grid, row, col, val):
    inRow = checkInRow(grid, row, val)
    inCol = checkInCol(grid, col, val)
    inBox = checkInBox(grid, row - (row%3), col - (col%3), val)
    if (not inRow and not inCol and not inBox):
        return True
    else:
        return False

def validGrid(grid):
    if (not validFormatting(grid)):
        return None
    elif (
            validRows(grid) and
            validCols(grid) and
            validBoxes(grid)
            ):
        return True
    else:
        return False

def solveSudoku(grid):
    nextSpot = getOpenSpot(grid)
    if (nextSpot == None):
        return True

    row = nextSpot[0]
    col = nextSpot[1]
    for digit in range(1,10):
        if (checkIsOkay(grid, row, col, digit)):
            #print("Selected:", digit)
            grid[row][col] = digit
            #printGrid(grid)
            if (solveSudoku(grid)):
                return True
            else:
                grid[row][col] = 0
    return False

