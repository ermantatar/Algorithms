from ast import List
class Solution:
    def two_sum(self, nums: List[int], target: int) -> int:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [i, hash_map[complement]]
            
            hash_map[nums[i]] = i

        #t: (N)
        #s: (N)
