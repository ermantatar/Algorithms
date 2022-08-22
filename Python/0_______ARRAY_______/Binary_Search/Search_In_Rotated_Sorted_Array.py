from ast import List

"""
Algorithm: 
Since this is a sorted array even though it is a rotated, we can utilize the binary search here. 
As always, we run the loop with left <= right, and calculate the min = left + (right - left) // 2
Check if mid == target, then return mid
Main intiution is to chase target in the correct sequence area, like 2,3,4,5,6,7 find target here, or 1,2,3,4,5 instead 6,7,1,2,3 in this area should be else statements.
nums[left] <= nums[mid]
      if nums[left] <= target < nums[mid]: right = mid -1 else left = mid + 1
nums[left] > nums[mid]
      nums[mid] < target <= nums[right]
"""

class Solution:
    # t: O(LogN)
    # s: O(1)
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                
        # Main if-else scenarios
        # [3][4][5][6][7][8][9][1][2]
        # [8][7][6][5][4][3][2][1][9]