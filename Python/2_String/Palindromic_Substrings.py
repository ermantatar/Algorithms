class Solution:
    def expandAroundCenter(self, s: str, l: int, r: int)->int:
        
        ans = 0
        while (0 <= l and r < len(s) and s[l] == s[r]):
            l -=1
            r += 1
            ans += 1
        
        return ans
    
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s)):
            # odd-amount palindromes
            ans += self.expandAroundCenter(s, i, i)
            # even-amount palindromes
            ans += self.expandAroundCenter(s, i, i+1)
            
        return ans
    
    # t: O(N ^ 2)
    # s: O(1)