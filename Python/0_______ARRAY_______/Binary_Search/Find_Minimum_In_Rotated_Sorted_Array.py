from ast import List

# Algorithm
# Since array is sorted even though it is rotated, we can utilize the binary search.
# First, check if there is only one item, if so return it
# Second, check left = 0, right = length-1, and array[left] < array[right], then no rotation, return array[left]
# After that while loop with left <= right, and get mid = left + (right - left) // 2
# Check if, nums[mid] > nums[mid+1]: return nums[mid+1]
# Check if, nums[mid-1] > nums[mid]: return nums[mid]

# left = mid + 1 if nums[0] < nums[mid] else right = mid - 1 

class Solution:
    # t: O(LogN), s: O(1)
    def findMin(self, nums: 'List[int]') -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        # There might not be a rotation at all, check this! 
        if nums[l] < nums[r]:
            # there is no rotation
            return nums[l]
        
        while l <= r:
            
            m = l + (r - l) // 2
            
            # There is only, 7,1 case where nums[i] > nums[i+1]
            # 4,5,6,[7],1,2,3,
            if nums[m] > nums[m+1]:
                return nums[m+1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # Where could be lowest located in this sequence? 
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1