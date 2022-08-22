from ast import List
class Solution:
    # Algorithm
    # Create a hash_map, iterate over array with indexes. 
    # check complement = target - nums[i] is in hashtable, is so return [i, hashtable[complement]]
    # If not, record all the numbers in hash table with their indexes as values hashtable[nums[i]]=i
    #t: (N)
    #s: (N)
    def two_sum(self, nums: List[int], target: int) -> int:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [i, hash_map[complement]]
            
            hash_map[nums[i]] = i

        
