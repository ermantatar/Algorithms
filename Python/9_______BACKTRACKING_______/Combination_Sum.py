"""
    Given distinct int array & a target, return list of all unique combos that sum to target
    Ex. candidates = [2,3,6,7] target = 7 -> [[2,2,3],[7]]

    Backtracking, generate all combo sums, push/pop + index checking to explore new combos

    Time: O(n^target)
    Space: O(target)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return 
            elif i >= len(candidates) or total > target:
                return 
            
            # include the current index's number 
            subset.append(candidates[i])
            dfs(i, subset, total + candidates[i])
            
            # Not include the current index's number
            subset.pop()
            dfs(i+1, subset, total)
        
        dfs(0, [], 0)
        return res