class Solution:
	# Negating the indices to make it seen! 
    # t: O(N)
    # s: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            # new index from the current index
            new_index = abs(nums[i]) - 1
            
            if nums[new_index] > 0:
                nums[new_index] *= -1
            
        missing_numbers = []
        
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

		for num in range(1, len(nums)+1):
			if num not in hash_table:
				result.append(num)

		return result
