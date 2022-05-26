class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}
        res = L = 0
        
        for R in range(len(s)):
            
            curr_char = s[R]
            
            if curr_char in seen:
                seen[curr_char] += 1
            else:
                seen[curr_char] = 1
            
            
            if (R - L + 1) - max(seen.values()) <= k:
                res = max(res, R - L + 1)
            else:
                seen[s[L]] -= 1
                L += 1
        
        return res
    # t: O(N)
    # s: O(N)
    

        