from ast import List

class Solution:
    # Since it is sorted, we can utilize the two-pointers approach.  
    # First, create the low and high pointers, and calculate their sum, 
    # If two pointers value smaller then target, then move left to right with +1, or decrease -1 
    # t: O(N)
    # s: O(1)
    def twoSum2(self, nums: List[int], target: int)->int:

        l, r = 0, len(nums)-1

        while l < r:

            total_sum = nums[l] + nums[r]
            
            if total_sum == target:
                return (l+1, r+1)
            elif total_sum < target:
                l += 1
            else:
                r -= 1

        return [-1, 1]
    
    