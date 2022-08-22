# Question 
# Given nums with length n, all integers are [1, n]. 
# Each integer will appear once or twice, find the duplicate ones. 

# Iterate over the array and for every element x in the array, negate the value at index array[abs(x)-1], 
# check this array[abs(x)-1] is negative before. If so, duplicate!!! Add to the result array
# The negation operation effectively marks the value abs(x) as seen / visited.

class Solution:
	# t: O(N)
	# s: O(N) - output list might not be counted as extra space. 
	def findDuplicates(self, nums: List[int]) -> List[int]:
		res = []
		for num in nums:
			if nums[abs(num) - 1] < 0: # seen before
				res.append(abs(num))
			else: # never seen, sign it 
				nums[abs(num) - 1] *= -1

		return res 




# Here Pythoner code, but using extra space. 
class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		# return [key for key, value in collections.Counter(nums).items() if value == 2]

		res = []
		for key, value in collections.Counter(nums).items():
			if value == 2:
				res.append(key)