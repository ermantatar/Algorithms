class Solution:
    # t: O(N)
    # s: O(N)
    def isPalindrome2(self, s: str) -> bool:
        
        filtered_chars = filter(lambda c: c.isalnum(), s)
        
        lowercase_filtered_chars = map(lambda c: c.lower(), filtered_chars)
        
        filtered_chars_list = list(lowercase_filtered_chars)
        
        reversed_chars_list = filtered_chars_list[::-1]
        
        return filtered_chars_list == reversed_chars_list
    
    # t: O(N)
    # s: O(1)
    def isPalindrome(self, s:str) -> bool:
        
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False 
            
            left += 1
            right -= 1
        
        return True
