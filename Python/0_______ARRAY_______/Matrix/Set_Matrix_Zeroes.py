from ast import List
class Solution:
    # t: O(m * n)
    # s: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # top north 0 sign it.
                    matrix[0][c] = 0
                    if r > 0:
                        # First column sign 
                        matrix[r][0] = 0
                    else:
                        # this is only for the r = 0 case. 
                        # first row sign
                        rowZero = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
    
"""
[q][w][e][r]
[t][y][u][i]
[o][p][a][s]
[d][f][g][h]
"""
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # input validation
        if not matrix:
            return []

        ROWS = len(matrix)
        COLS = len(matrix[0])

        zeroes_row = [False] * ROWS
        zeroes_col = [False] * COLS

        for row in range(ROWS):
            for col in range(COLS):
                 if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True

        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
        

    




'''
- Do not modify in place of input matrix, since it might create domino effect
- If we turn 1's into zereos because we've seen previous zeroes on the row, then 
- all of a sudden, that 1->0 will trigger its own column and rows to turn zero. 
'''