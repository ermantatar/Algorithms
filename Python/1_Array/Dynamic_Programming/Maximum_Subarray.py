from ast import List 
class Solution:
    def maximumSubarray(self, nums: List[int])->int:
        
        current_sum, maximum_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            maximum_sum = max(maximum_sum, current_sum)
        
        return maximum_sum
    # t: O(N)
    # s: O(1)
    