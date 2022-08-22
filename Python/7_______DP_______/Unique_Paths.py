class Solution:
    # DFS with cache
    # T: O(m * n), S: O(m * n)
    def uniquePaths(self, m, n):
        @cache 
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            if r == m-1 or c == n-1:
                return 1
            
            return dfs(r+1, c) + dfs(r, c+1)

        return dfs(0, 0)

    
    # Dynamic Programming 
    # t: O(m * n) s:O(m*n)
    def uniquePaths(self, m, n):
        dp = [[1] * n for row in range(m)]

        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]