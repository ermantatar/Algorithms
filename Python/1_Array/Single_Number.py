from ast import List
from collections import defaultdict

class Solution:
    def single_numer(self, nums: List[int])-> int:
        no_duplicate_list = []
        for num in nums:
            if num not in no_duplicate_list:
                no_duplicate_list.append(num)
            else:
                no_duplicate_list.remove(num)
        return no_duplicate_list.pop()
    # t: O(n^2)
    # s: O(n)

    def single_number2(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] += 1
        
        for num in hash_table:
            if hash_table[num] == 1:
                return num 
    # t: O(N)
    # s: O(N)

    
    def single_number3(self, nums: List[int]) -> int:
        #math 2 (a + b + c) - (a + a + b + b + c)
        return 2 * sum(set(nums)) - sum(nums)
    # t: O(N)
    # s: O(N), set needs new space to store all elements. 


    def single_number4(self, nums: List[int])->int:
        result = 0
        for num in nums:
            result ^= num
        return num 
    
    # t: O(N)
    # s: O(1)






    

