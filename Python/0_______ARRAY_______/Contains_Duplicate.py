from ast import List


#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


"""
1
Brute Force Approach 
t: O(N ^ 2) s: O(1)
"""
def find_duplicates_bruteforce(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True 
    
    return False 

"""
2
Sorting 
t: O(NlogN) s: O(1)
"""
def duplicate_sorting(nums):
    nums.sort()
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True 
    
    return False 
"""
3
# Hashmap / Hashset 
t: O(N) and s: O(N)
"""
def duplicate_4(nums):

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False 

"""
4
Set and Original Comparison
t: O(N) and s: O(N)
"""

def duplicate_5(nums):
    nums_set = set(nums)
    return len(nums) == len(nums_set)

"""
5
Using collections.counter()
t: O(N) s:(N)
"""
import collections 
def duplicate_6(nums):
  count_dict = collections.Counter(nums).items()
  print([item for item, count in count_dict if count > 1])





if __name__ == "__main__":
  nums = [4,6,1,8,10,4]
  k = 3
  print(duplicate_4(nums))

