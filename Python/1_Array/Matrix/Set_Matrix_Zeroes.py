from ast import List
class Solution:
    def setZeroes(self, matrix: List[List[int]])->None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False 

        #determine which rows and columns need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] == 0
                    if r > 0:
                        matrix[r][0] = 0 # because we determined the [0][0] already for a variable.
                    else:
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
        

    # s: O(1)




'''
- Do not modify in place of input matrix, since it might create domino effect
- If we turn 1's into zereos because we've seen previous zeroes on the row, then 
- all of a sudden, that 1->0 will trigger its own column and rows to turn zero. 
'''