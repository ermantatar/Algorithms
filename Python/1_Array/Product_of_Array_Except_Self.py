from ast import List

class Solution:
    def productExceptSelf(self, nums: List[int])->List[int]:

        length = len(nums)
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] will contain all the product of elements on the left side. L[0] = 1
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1] * L[i-1]
        
        # R[i] contains the product of all the elements to the right, R[Length-1] = 1
        R[length-1] = 1
        for i in reversed(range(length-1)):
            R[i] = nums[i+1] * R[i + 1]
        
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer
    # t: O(N)
    # s: O(N)

    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        answer = [0] * length 

        answer[0] = 1
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i - 1]

        R = 1
        for i in reversed(range(length-1)):
            answer[i] = nums[i+1] * R 
            R*= answer[i]
        
        return answer
    # t: O(N)
    # s: O(1)
        



