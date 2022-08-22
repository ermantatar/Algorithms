from ast import List


class Solution:
    # t: O(MxN), number of cell in the grid.
    # s: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
        
    
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
    

# There is also another solution
# https://leetcode.com/problems/rotate-image/solution/

"""
[q][w][e][r]
[t][y][u][i]
[o][p][a][s]
[d][f][g][h]

[d][o][t][q]
[f][p][y][w]
[g][a][u][e]
[h][s][i][r]
"""