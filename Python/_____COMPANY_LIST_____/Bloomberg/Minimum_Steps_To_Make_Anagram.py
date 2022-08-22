class Solution:
    # t: O(N), s: O(N)
    def minSteps(self, s: str, t: str) -> int:

        counterS, steps = Counter(s), 0

        for char in t:
            if counterS[char] > 0:
                counterS[char] -= 1
            else:
                steps += 1
        
        return steps 
    
    # We don't need to count leftovers at CounterS, since it will be duplicate to count aab bba, one change is fine, we don't need 2 change here. 

    def minSteps_Short(self, s: str, t: str) -> int:

        cnt1, cnt2 = map(collections.Counter, (s, t))
        return sum(abs(cnt1[c] - cnt2[c]) for c in string.ascii_lowercase) // 2
    
    def minSteps(self, s: str, t: str) -> int:
        cnt1, cnt2 = map(collections.Counter, (s, t))
        return sum((cnt1 - cnt2).values())

        