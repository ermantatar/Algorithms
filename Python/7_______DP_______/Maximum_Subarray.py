from ast import List 

class Solution:
    """
    Algorithm:
    Define current_sum and maximum_sum and assign the first item of nums[0]
    Loop over the nums[1:], starting from the first index 
    
    """
    # t: O(N)
    # s: O(1)
    def maximumSubarray(self, nums: List[int])->int:
        
        current_sum, maximum_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            maximum_sum = max(maximum_sum, current_sum)
        
        return maximum_sum
    
    