
# Given nums with length n, all integers are [1, n]. 
# Each integer will appear once or twice, find the duplicate ones. 

class Solution:
	# t: O(N)
	# s: O(N) - output list might not be counted as extra space. 
	def findDuplicates(self, nums: List[int]) -> List[int]:
		res = []
		for num in nums:
			if nums[abs(num) - 1] < 0:
				res.append(abs(num))
			else:
				nums[abs(num) - 1] *= -1

		return res 




# Here Pythoner code, but using extra space. 
class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		return [key for key, value in collections.Counter(nums).items() if value == 2]
	