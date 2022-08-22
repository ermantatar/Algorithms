class Solution:
    # t: O(sum(N))
    # s: O(sum(N))
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False 
        
        target = total_sum // 2
        DP = set()
        DP.add(0)
        
        for num in nums:
            newDP = DP.copy()
            for ts in DP:
                if num + ts == target:
                    return True 
                newDP.add(num+ts)
                newDP.add(num)
            DP = newDP
        
        return False 

"""
Algorithm:

Decleare DP as a set, and iterate over the nums, add each number with numbers in set.
If you see any sum == total_sum // 2 return True 


"""

