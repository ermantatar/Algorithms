class Solution:
    # t: O(n * m * n)
    # s: O(n)
    # [n _ T][e _ F][e _ F][t _ F][c _ T ][o _ F][d _ F][e _ F][T]
    def wordBreak_DP(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True 

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: # if there is w match, break and move new loop no need to check again.
                    break;
        
        return dp[0]
# Continue to read the solution, there are more solution for this link.
# https://leetcode.com/problems/word-break/