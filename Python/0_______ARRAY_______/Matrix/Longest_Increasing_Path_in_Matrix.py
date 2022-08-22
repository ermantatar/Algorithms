from typing import List


class Solution:
    """
        DP_Question
        Given matrix, return length of longest increasing path
        Ex. matrix = [[9,9,4],[6,6,8],[2,1,1]] -> 4, [1,2,6,9]

        DFS + memo, cache on indices, compare to prev for increasing check

        Time: O(m x n)
        Space: O(m x n)
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0 
        
        dp = {} # k: (r, c): LongestIncreasingPath
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        def dfs(r, c, prevVal):
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            
            dp[(r, c)] = res 
            return res 
        
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        
        return max(dp.values())