class Solution:
    
    # t: O(N)
    # s: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        # what is the sum of numbers from [0.....N] = ((N * N + 1) / 2)
        # Apply the formula here! 
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    

    # t: O(NlogN)
    # s: O(N)
    def missingNumber(self, nums):
        # we need to sort array so that we can compare [i-1][i], because nums[i] = nums[i-1] + 1
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num