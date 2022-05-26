class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        l = 0
        res, resLen = [-1, -1], float("infinity")
        
        
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                #update our result 
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1 )
                # pop from the left and shrink the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                    
                l +=1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""