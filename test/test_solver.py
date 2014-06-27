#!/usr/local/bin/python3

import unittest
import boards
import solver

class TestBacktrackSolver(unittest.TestCase):

    def test_validFormatting(self):
        goodGrid = boards.valid
        badGrid = boards.ill_formed

        #Good Grids
        self.assertTrue(solver.validFormatting(goodGrid))

        #Bad Grids
        self.assertFalse(solver.validFormatting(badGrid))

    def test_validRows(self):
        goodGrid = boards.valid
        badGrid = boards.invalid

        #Good Grids
        self.assertTrue(solver.validRows(goodGrid))

        #Bad Grids
        self.assertFalse(solver.validRows(badGrid))

    def test_validCols(self):
        goodGrid = boards.valid
        badGrid = boards.invalid_2

        #Good Grids
        self.assertTrue(solver.validCols(goodGrid))

        #Bad Grids
        self.assertFalse(solver.validCols(badGrid))

    def test_validBoxes(self):
        goodGrid = boards.valid
        badGrid= [[5,3,4,6,7,8,9,1,2],
                  [6,7,2,1,9,5,3,4,8],
                  [1,9,8,3,4,2,5,6,7],
                  [8,5,9,7,6,1,4,2,3],
                  [4,2,6,8,5,3,7,9,1],
                  [7,0,3,9,2,4,1,5,6],
                  [9,6,1,5,3,7,2,8,4],
                  [2,8,7,4,1,9,6,3,5],
                  [3,4,5,2,8,1,0,7,9]]

        #Good Grids
        self.assertTrue(solver.validCols(goodGrid))

        #Bad Grids
        self.assertFalse(solver.validCols(badGrid))

    def test_checkInRow(self):
        goodGrid = [[1,2,3,4,5,6,7,8,9],
                    [4,5,6,7,8,9,1,2,3],
                    [7,8,9,1,2,3,4,5,6],
                    [2,3,4,5,6,7,8,9,1],
                    [5,6,7,8,9,1,2,3,4],
                    [8,9,1,2,3,4,5,6,7],
                    [3,4,5,6,7,8,9,1,2],
                    [6,7,8,9,1,2,3,4,5],
                    [9,1,2,3,4,5,6,7,8]]

        #Good Grids
        self.assertFalse(solver.checkInRow(goodGrid, 4, 0))

        #Bad Grids
        self.assertTrue(solver.checkInRow(goodGrid, 4, 9))




if __name__ == "__main__":
    unittest.main()

