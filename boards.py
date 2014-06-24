#!/usr/local/bin/python3

ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

ill_formed_2 = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,"a",4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]

valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,4,2,6,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

invalid_2 = [[5,3,4,6,7,8,9,1,2],
             [6,7,2,1,9,5,3,4,8],
             [1,9,4,3,8,2,5,6,7],
             [8,5,9,7,6,1,4,2,3],
             [4,2,6,8,5,3,7,9,1],
             [7,1,3,9,2,4,8,5,6],
             [9,6,1,5,3,7,2,8,4],
             [2,8,7,4,1,9,6,3,5],
             [3,4,5,2,8,6,1,7,9]]

invalid_3 = [[5,3,4,6,7,8,9,1,2],
             [6,7,2,1,9,5,3,4,8],
             [1,9,8,3,4,2,5,6,7],
             [8,5,9,7,6,1,4,2,3],
             [4,2,6,8,5,3,7,9,1],
             [7,0,3,9,2,4,1,5,6],
             [9,6,1,5,3,7,2,8,4],
             [2,8,7,4,1,9,6,3,5],
             [3,4,5,2,8,6,0,7,9]]

easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,6,0,2,0,0,0,8],
        [0,0,0,6,0,0,5,0,0],
        [0,0,0,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]


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
    for row in grid:
        bit_list = [False] * 10;
        for current_item in row:
            if(bit_list[current_item]):
                print("{0} was duplicated in row {1}".format(current_item, row))
                return False
            else:
                bit_list[current_item] = True

    # Check columns
    for c in range(len(grid[0])):
        bit_list = [False] * 10;
        for r in range(len(grid)):
            current_item = grid[r][c]
            if(bit_list[current_item]):
                print("{0} was duplicated in column {1}".format(current_item, r))
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
        for c in range(3):
            for r in range(3):
                current_item = grid[y+r][x+c]
                if(bit_list[current_item]):
                    print("{0} was duplicated in box ({1},{2})".format(current_item, x//3, y//3))
                    return False
                else:
                    bit_list[current_item] = True


    return True


print(check_sudoku(ill_formed))
print(check_sudoku(ill_formed_2))
print(check_sudoku(valid))
print(check_sudoku(invalid))
print(check_sudoku(invalid_2))
print(check_sudoku(invalid_3))
print(check_sudoku(easy))
print(check_sudoku(hard))

