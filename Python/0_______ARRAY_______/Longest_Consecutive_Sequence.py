# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence
# nums = [100,4,200,1,3,2] => 4

# Algorithm:
# Turn input array into set, set(nums) this will allow is O(1) lookup time
# Iterate over the set(nums) and check if num-1 is not in set(nums), if so, this will be initial number in the consecutive numbers, initial, +1, +2, +3
# Record that, so far length is 1, then check if initial + 1, in the set, initial+2 in the set, check this in while loop condition and increase the query +1 every time.
# Always save the longest length after each longest subsequence, and return the max one!!  
class Solution:
    # t: O(n + n) = O(N) not O(n^2) because only first item of sequence can make into if condition.
    # s: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0 
        
        longest_sequence = 0
        num_set = set(nums) # so that it can give us O(1) lookup time!
        
        for num in num_set:
            # only pick numbers that are initial of all sequences. 
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence +=1
                
                longest_sequence = max(longest_sequence, current_sequence)
        
        return longest_sequence
                
    
    
    # t: O(NlogN)
    # s: O(1)
    def longestConsecutive_Sorting(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        
        nums.sort()
        
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                if nums[i-1] + 1 == nums[i]:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
                    
        # since last item might be part of the longest streak 
        return max(longest_streak, current_streak)
    
    
    # Brute Force 
    # t: O(N^3)
    # s: O(1)
    def longestConsecutive_BruteForce(self, nums: List[int]) -> int:
        longest_streak = 0
        
        for num in nums:
            current_num = num 
            current_streak = 1
            
            while current_num + 1 in nums:
                current_num +=1 
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
        
        return longest_streak 
    