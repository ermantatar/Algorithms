class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""
        
        windowS, countT = {}, {}
        
        for c in t:
            countT[c] = countT.get(c, 0) + 1  
        
        res, resLen = [-1, 1], float("inf")
        
        have, required = 0, len(countT)
        
        l = 0
        for r, curr_char in enumerate(s):
            
            # add char to windowS and compare with countT
            windowS[curr_char] = windowS.get(curr_char, 0) + 1
            if curr_char in countT and countT[curr_char] == windowS[curr_char]:
                have += 1
            
            # if we have enough for what is required, then we will optimize by trying to shrink window
            while have == required:
                # check if we capture the minimum so far!
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                
                # try to shrink the window
                # Since l index item, s[l] will be gone, reduce it from the windowS
                windowS[s[l]] -= 1
                if s[l] in countT and windowS[s[l]] < countT[s[l]]:
                    have -= 1
                    
                l+=1
        
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""