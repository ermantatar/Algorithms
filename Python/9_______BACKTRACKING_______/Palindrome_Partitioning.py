"""
    Given a string, partition such that every substring is a palindrome, return all possible ones
    Ex. s = "aab" -> [["a","a","b"],["aa","b"]], s = "a" -> [["a"]]

    Generate all possible substrings at idx, if palindrome potential candidate, backtrack after

    Time: O(n x 2^n)
    Space: O(n)
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(s):
                res.append(subset[:])
                return 
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
        
        dfs(0)
        return res 
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1
        return True 