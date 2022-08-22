class Solution:
    # t: O(LogN), s:(1)
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r-l) // 2
            
            if nums[m] == target:
                return m
            else if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return -1