"""
    Given an integer array of unique elements, return all possible subsets (the power set)
    Ex. nums = [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]]

    Backtracking, generate all combos, push/pop + to explore new combos, skip duplicates

    Time: O(n x 2^n)
    Space: O(n)
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # keep duplicates next to each other
        nums.sort()
        
        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset[:])
                return 
            
            # decision to include the current index's number
            subset.append(nums[i])
            backtrack(i+1, subset)
            
            # decision to NOT include the current index's number
            subset.pop()
            
            # remember duplicates right here! 
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, subset)
        
        
        
        backtrack(0, [])
        return res 