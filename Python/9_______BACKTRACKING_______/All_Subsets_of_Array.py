"""
    Given an integer array of unique elements, return all possible subsets (the power set)
    Ex. nums = [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Backtracking, generate all combinations, push/pop + index checking to explore new combos

    Time: O(n x 2^n)
    Space: O(n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # decision to include the current index's val
            subset.append(nums[i])
            dfs(i+1)
            
            # decision to NOT include the current index's val
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res