from ast import List

class Solution:
    def twoSum2(self, nums: List[int], target: int)->int:

        low, high = 0, len(nums)-1
        while low < high:
            total_sum = nums[low] + nums[high]
            if total_sum == target:
                return (low+1, high+1)
            elif total_sum < target:
                low += 1
            else:
                high -= 1

        return [-1, 1]
    
    # t: O(N)
    # s: O(1)