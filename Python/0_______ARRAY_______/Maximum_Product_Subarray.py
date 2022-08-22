from ast import List

# Algorithm:
# Records first item as max_so_far, min_so_far, and iterate starting from range(1, len(nums))
# Every iteration, save current number, curr, check two condition; 
#   @ temp_max_so_far = max(curr, curr * max_so_far, curr * min_so_far)
#   @ min_so_far = min(curr, curr * max_so_far, min_so_far)
#   and save the max_so_far = temp_max_so_far, and then record the result_max = max(result_max, max_so_far), then return result!! 

class Solution:
    # t: O(N)
    # s: O(1)
    def maxProductOfSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]

        result = max_so_far

        for curr in nums[1:]:
            
            # we want to use tmp variable, since min_so_far is dependent on the previos value of max.
            round_max = max(curr, max_so_far * curr, min_so_far * curr)
            round_min = min(curr, curr * max_so_far, curr * min_so_far)

            max_so_far = round_max
            min_so_far = round_min
            result = max(result, max_so_far)

        return result 
    