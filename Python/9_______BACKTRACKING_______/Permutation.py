"""
    Given array of distinct integers, return all the possible permutations
    Ex. nums = [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Permute by swapping i/start, DFS from this point, backtrack to undo swap

    Time: O(n x n!)
    Space: O(n!)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # base case 
        if len(nums) == 1:
            return [nums[:]]
        
        res = []
        for i in range(len(nums)):
            # 1 [2, 3]
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
                res.append(perm)
            
            nums.append(n)
        
        return res 