"""
    Given 2 strings s & t:
    Return # of distinct subsequences of s which equals t
    Ex. s = "rabbbit", t = "rabbit" -> 3, RABBbIT, RAbBBIT, RABbBIT

    DFS + memo, cache on i & j indices to the # of distinct subseq
    2 choices: if chars equal, look at remainder of both s & t
               if chars not equal, only look at remainder of s

    Time: O(m x n)
    Space: O(m x n)
"""
class Solution:
    def numDistinct(self, s, t):
        cache = {}
        def dfs(i, j):
            if j == len(t): 
                return 1
            if i == len(s): 
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]: 
                cache[(i, j)] = dfs(i+1, j) + dfs(i+1, j+1)
            else:
                cache[(i, j)] = dfs(i+1, j)
            
            return cache[(i, j)]

        return dfs(0, 0)