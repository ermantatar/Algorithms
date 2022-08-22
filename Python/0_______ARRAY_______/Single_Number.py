from ast import List
from collections import defaultdict

class Solution:
    # Algorithm:
    # We can use hash_table to keep track of occurences of keys
    # The key has 1 as a value, will be single number! return it.

    # t: O(N)
    # s: O(N)
    def single_number(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1
        
        for key, value in counter.items():
            if value == 1:
                return key
    

    # t: O(N)
    # s: O(N), set needs new space to store all elements. 
    def single_number(self, nums: List[int]) -> int:
        #math 2 (a + b + c) - (a + a + b + b + c)
        return 2 * sum(set(nums)) - sum(nums)
    

    # while looking for the single occurance number, if I want to optimize the space usage,
    # I can xor all numbers, since number neuteralize themselves, the one left will be single value
    # for num in nums: result ^= num, then return the result
    def single_number(self, nums: List[int])->int:
        result = 0
        for num in nums:
            result ^= num
        return result 
    
    # t: O(N)
    # s: O(1)






    

