class Solution:
    # t: O(N) and s: O(1) since alphanet has hard limit 26. 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        # Decleare two arrays with 26 [0,0,0...0] for each char index
        s1Count, s2Count = [0] * 26, [0] * 26
        # Go through the a-z chars, by looping 0 to 26 index, increase the index in two array so that char_index: count 
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Loop through the 0 to 26, and check if two array has the same count for same char_index, if so, increase matches amount. 
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # Decleare the left ptr, and since we already looped first len(s1)-1 part, start from len(s1) 
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            # Extend the window by right ptr, and handles the matches (if there is already mismatch, don't need to anything. )
            # Handle two case, if this current round gives us a match, or break previous match. 
            index = ord(s2[r]) - ord('a') # get current round char's index
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # Shrink the window by left ptr, and handles the matches 
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
            