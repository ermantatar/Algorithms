class Solution:
    # Sliding Window
    # t: O(N)
    # s: O(N)
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        res = 0

        l = 0
        for r, char in enumerate(s):
            
            if char in window:
                window[char] += 1
            else:
                window[char] = 1
            
            # ABCXB, I can eliminate only 2, then [BCXB], we can eliminate CX, max window result is 4. 
            if (r - l + 1) - max(window.values()) <= k: # if other characters amount less than k? nice, save this window lenght. 
                res = max(res, r - l + 1)
            else:
                # If there is more than allowed amount of character, then shrink the window, and remove l's item from the window. 
                window[s[l]] -= 1
                l += 1
        
        return res

 
    

        