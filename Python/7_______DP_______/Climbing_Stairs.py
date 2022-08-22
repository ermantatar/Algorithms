class Solution:
    def climbStairs(self, n: int) -> int:
        # Start 
        # [1][1][2][3][5][8]
        
        DP = [0] * (n + 1) 
        
        DP[0] = 1
        DP[1] = 1
        
        for i in range(2, n+1):
            DP[i] = DP[i-1] + DP[i-2]
        return DP[n]