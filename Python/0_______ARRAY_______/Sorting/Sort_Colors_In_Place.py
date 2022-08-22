class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        l, r = 0, len(nums)-1
        i = 0
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
                # Do not increment i here, since it can introduce 0s to stay in the middle. 
            i = i+1 