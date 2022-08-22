class Solution:

	# Negating the indices to make it seen! 
    # t: O(N)
    # s: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            # sign (current number -1)'th index
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            
        missing_numbers = []
        # N -> [1, ....N], loop len(nums) + 1
        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0:
                missing_numbers.append(i)
                
        return missing_numbers


	# t: O(N)
	# s: O(N)
	def findDisappearedNumbers(self, nums):
		
		hash_table = {}

		for num in nums:
			hash_table[num] = 1 

		missing_numbers = []
		for num in range(1, len(nums)+1): # [numbers starts from 1, there is no 0]
			if num not in hash_table:
				missing_numbers.append(num)

		return missing_numbers
