from ast import List

class Solution:
    def maxProductOfSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]

            temp_max_so_far = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, curr * max_so_far, curr * min_so_far)

            max_so_far = temp_max_so_far
            result = max(result, max_so_far)

        result 
    # t: O(N)
    # s: O(1)