from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False
    # t: O(N)
    # s: O(N)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num in dict:
                return True 
            else:
                dict[num] = 1
        
        return False
    # t: O(N)
    # s: O(N)

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return True 
        
        return False 
    # t: O(N)
    # s: O(1)


'''
Sorting Notes: 
    If we want to sort by specific property of the object. 
    => sort(key=lambda student: student[2])

    sorted(list) or list.sort()
'''
