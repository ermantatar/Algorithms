class Solution:
    
    def wordBreak_DP(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True 

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break;
        
        return dp[0]
    # t: O(n^3)
    # s: O(n)
# Continue to read the solution, there are more solution for this link.
# https://leetcode.com/problems/word-break/