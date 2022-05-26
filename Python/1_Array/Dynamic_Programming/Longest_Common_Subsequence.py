class Solution:
    # clear solution
    def longestCommonSubsequence(self, text1: str, text2: str) -> bool:
        dp = [[ 0 for col in range(len(text2) + 1)] for row in range(len(text1) + 1)]

        for row in range(len(text1)-1, -1, -1):
            for col in range(len(text2)-1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        
        return dp[0][0]
    # t: O(n * m)
    # s: O(n * m)

    # Space Optimization
    def longestCommonSubsequence2(self, text1: str, text2: str) -> bool:
        
        if (len(text1) > len(text2)):
            text1, text2 = text2, text1

        previousCol = [0] * (len(text1) + 1)
        currentCol = [0] * (len(text1) + 1)

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    currentCol[row] = 1 + previousCol[row + 1]
                else:
                    currentCol[row] = max(previousCol[row], currentCol[row+1])

            previousCol, currentCol = currentCol, previousCol
        
        return previousCol[0]

    # t: O(n * m)
    # s: O(min(n, m))
        


# Read leetcode article one more time, it was very well prepared! 


'''
Here is the dp grid, in the second optimization, we are using only two column, since we are only iterating through them. 
No, need to keep whole dp matrix in the memory.
       t  e  x  t  2  0
    t [ ][ ][ ][ ][ ][0]
    e [ ][ ][ ][ ][ ][0]
    x [ ][ ][ ][ ][ ][0]
    t [ ][ ][ ][ ][1][0]
    1 [ ][ ][ ][ ][1][0]
    0 [0][0][0][0][0][0]
'''