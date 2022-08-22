class Solution:
    """
        Given a string w/ only digits, return # ways to decode it (letter -> digit)
        Ex. s = "12" -> 2 (AB 1 2 or L 12), s = "226" -> 3 (2 26 or 22 6 or 2 2 6)

        DP: At each digit, check validity of ones & tens, if valid add to # ways
        Recurrence relation: dp[i] += dp[i-1] (if valid) + dp[i-2] (if valid)

        Time: O(n)
        Space: O(n)
    """
    def numDecodings(self, s: str) -> int:
        
        # Dynamic Programming
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]

        return dp[0]
    
    ## NEETCODE ## Solutions: 
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                return 0
            
            # one step
            res = dfs(i + 1)
            
            # check second step, 1[0-9] but 2[0-6] since max rep value is 26
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
                
            # cache the result
            dp[i] = res
            return res

        return dfs(0)

test_obj = Solution()

print(test_obj.numDecodings("123")) #1,2,3 - 12, 3 - 1, 23 
        