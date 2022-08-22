class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def backtrack(i, total):
            # base case: 
            if i == len(nums):
                return 1 if total == target else 0
            
            # base case: if it is in the cache! 
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i]) 

            return dp[(i, total)]

        # start from index 0 with total 0
        return backtrack(0, 0)







"""
nums = [1,1,1,1,1], target = 3

How many ways we can reach target with adding or removing every single item. 
These both count as unique ways, so we need to have DFS decision tree with caching
1+1+1-1+1 = 3
1-1+1+1+1 = 3

"""