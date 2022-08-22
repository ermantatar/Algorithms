
# This is house robber I and house robber II questions
class Solution:
    def rob_II(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        # Since array is circular this time, we can't have the 0'th index -1'th index the same time in the solution.
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
    
    # t: O(N), s:O(1)
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for house in nums:
            tmp = max(rob1 + house, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2 
    
"""
        [1, 2, 3, 1]
        rob1:0,0,1...
        rob2:0,1,2...
"""     

