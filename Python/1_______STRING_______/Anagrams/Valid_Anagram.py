import collections

class Solution: 
    # t: O(NlogN), s: O(1)
    def isAnagram3(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
    # t: O(N) and s:O(N)
    def isAnagram2(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS = {}
        for c in s:
            mapS[c] = mapS.get(c, 0) + 1
        
        for c in t:
            if c not in mapS:
                return False
            else:
                mapS[c] -= 1
        
        for val in mapS.values():
            if val != 0:
                return False
        
        return True