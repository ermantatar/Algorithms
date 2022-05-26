from ast import List

class Solution:
    def rotate(self, matrix: List[List[int]])-> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
    # t: O(M), number of cell in the grid.
    # s: O(1)

# There is also another solution. 
# https://leetcode.com/problems/rotate-image/solution/
