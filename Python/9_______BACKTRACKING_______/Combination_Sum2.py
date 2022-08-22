"""
    Given array & a target, find all unique combos that sum to target, nums can only be used once
    Ex. candidates = [10,1,2,7,6,1,5], target = 8 -> [[1,1,6],[1,2,5],[1,7],[2,6]]

    Backtracking, generate all combo sums, push/pop + index checking to explore new combos

    Time: O(2^n)
    Space: O(n)
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # bring duplicates next to each other 
        candidates.sort()
        
        res = []
        total = 0
        
        def backtrack(pos, subset, total):
            if total == target:
                res.append(subset[:])
            if total > target:
                return 
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue 
                # decision to include the current candidate 
                subset.append(candidates[i])
                backtrack(i+1, subset, total + candidates[i])
                
                # decision to not include this candidate, and pick next one in next round
                subset.pop()
                prev = candidates[i]
        
        backtrack(0, [], total)
        return res 