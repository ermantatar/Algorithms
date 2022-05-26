from ast import List


class Solution:
    # t: O(LogN), s: (1)
    def findMin(self, nums: 'List[int]') -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        if nums[left] < nums[right]:
            # there is no rotation
            return nums[left]
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1