from ast import List

class Solution:
    
    # Algorithm
    # - First, define 3 array, L, R, answers with [0] * len(nums)
    # - L[0] = 1, and fill the L array by iterating range(1, length), L[i] = L[i-1] * nums[i-1]
    # - R[length-1] = 1, fill the R array by iterating reversed(range(length-1)), R[i] = R[i+1] * nums[i+1]
    # - Lastly, for answer array fill the range(length), answer[i] = L[i] * R[i]
    # t: O(N)
    # s: O(N)
    def productExceptSelf(self, nums: List[int])->List[int]:

        length = len(nums)
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] will contain all the product of elements on the left side. L[0] = 1
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1] * L[i-1]
        
        # R[i] contains the product of all the elements to the right, R[Length-1] = 1
        R[length-1] = 1
        for i in reversed(range(length-2)):
            R[i] = nums[i+1] * R[i + 1]
        
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer
    
    # Algorithm
    # - First, we can optimize the L to be answer array itself, no need to keep two different array.
    # - We can fill the left results, answer[0]=1, then range(1, length), answer[i] = answer[i-1] * nums[i-1]
    # - R = 1, we can reduce R array to be variable, so that we can keep accumulate the R values, such as, R *= nums[i]
    # - where for right side, we can do, answer[i] = answer[i] * R, then next line, R *= nums[i]

    # t: O(N)
    # s: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
    
        



