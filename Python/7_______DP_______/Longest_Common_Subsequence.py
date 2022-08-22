class Solution:

    # t: O(n * m)
    # s: O(n * m)
    def longestCommonSubsequence_BottomUp(self, text1: str, text2: str):
        
        DP = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for i, i_v in enumerate(text1):
            for j, j_v in enumerate(text2):
                DP[i + 1][j + 1] = 1 + DP[i][j] if i_v == j_v else max(DP[i+1][j], DP[i][j+1])
                
        
        return DP[-1][-1]
    
    # t: O(n * m)
    # s: O(n * m)
    def longestCommonSubsequence_TopDown(self, text1: str, text2: str) -> int:
        
        DP = [[0] * (len(text2) + 1) for row in range(len(text1) + 1)]
        
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                
                if text1[i] == text2[j]:
                    DP[i][j] = 1 + DP[i+1][j+1]
                else:
                    DP[i][j] = max(DP[i+1][j], DP[i][j+1])
        
        return DP[0][0]

    '''
    Here is the dp grid, in the second optimization, we are using only two column, since we are only iterating through them. 
    No, need to keep whole dp matrix in the memory.
           t  e  x  t  2  0
        t [ ][ ][ ][ ][ ][0]
        e [ ][ ][ ][ ][ ][0]
        x [ ][ ][ ][ ][ ][0]
        t [ ][ ][ ][ ][1][0]
        1 [ ][ ][ ][1][1][0]
        0 [0][0][0][0][0][0]
    '''
    
    # t: O(n * m)
    # s: O(n * m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for row in range(len(text1) + 1)]
        
        # Iterate up each column, starting from the last one.
        for row in (range(len(text1))):
            for col in (range(len(text2))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row+1][col+1] = 1 + dp_grid[row][col]
                # Otherwise they must be different...
                else:
                    dp_grid[row+1][col+1] = max(dp_grid[row][col+1], dp_grid[row+1][col])
        
        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[len(text1)][len(text2)]
    

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
More similar LCS problems:
1092. Shortest Common Supersequence and Solution
1062. Longest Repeating Substring (Premium).
516. Longest Palindromic Subsequence
1312. Minimum Insertion Steps to Make a String Palindrome
''' 

