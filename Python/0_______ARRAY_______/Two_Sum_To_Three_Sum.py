# Algorithm
# Decleare the res variable, and then we need to sort array
# The reason is, _,_,_ we want to remove a change that first digit will have same value
# [3,3,0,-3, 2], there are two [3, 0, -3], [3, 0, -3] happens if we are not careful. 
# Sorting the array and not allowing two 3 posibility for first _, we will be fine for duplicates.
 
# t: O(n^2) and s: O(N) for Py. Log(N) for Java
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        # we don't want to see duplicate values considered for the same position, this is why 
        # we need to sort the array and skip considering the same values for the same positions  
        # _, _, _
        for i, v in enumerate(nums):
            
            # we don't want same value takes places in the first location.
            if i > 0 and v == nums[i - 1]:
                continue
            
            # two pointer approach to find the rest of two digits, _, _
            l, r = i + 1, len(nums) - 1
            while l < r:

                if v + nums[l] + nums[r] > 0:
                    r -= 1
                elif v + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    # [-2, -2, 0, 0, 2, 2], if we hadle _,_,_ l side, 
                    # right side will be fine, we will remove duplicate change.
                    # Don't forget to skip the duplicates, like we did to first item. 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            
