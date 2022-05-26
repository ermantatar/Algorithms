from ast import List

class Solution:
    # t: O(LogN)
    # s: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
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