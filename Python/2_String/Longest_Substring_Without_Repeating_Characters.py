class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = R = res = max_len = 0
        window = {}
        
        while R < len(s):
            #current char r_c, and current index R
            curr_char = s[R]
            
            if curr_char in window: 
                if window[curr_char] >= L: 
                    L = window[curr_char] + 1
            
            window[curr_char] = R 
            max_len = max(max_len, R-L+1)
            R+=1
        
        return max_len


    
''' 
Note:-  
Commonly used tables are:
    int[26] for Letters 'a' - 'z' or 'A' - 'Z'
    int[128] for ASCII
    int[256] for Extended ASCII
'''