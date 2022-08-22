class Solution:
    # Sol: Create hash table and assign everyone its index. 
    # t: O(N)
    # S: O(N)
    def lengthOfLongestSubstringWithoutRepeatingCharacter(self, s: str) -> int:
        
        window = {}
        max_len = 0
        l = 0
        for r in range(len(s)):
            curr_char = s[r]
            
            # if curr_char is in the window
            if curr_char in window:
                # because we are not deleting previous entries in window, even tho left is moved on. w[......L.........R] could be like this. 
                if window[curr_char] >= l: 
                    l = window[curr_char] + 1
            
            # If curr_char is not in the window, window has all characters uniquely set.  
            window[curr_char] = r 
            max_len = max(max_len, r-l+1)
        
        return max_len


    
''' 
Note:-  
Commonly used tables are:
    int[26] for Letters 'a' - 'z' or 'A' - 'Z'
    int[128] for ASCII
    int[256] for Extended ASCII
'''