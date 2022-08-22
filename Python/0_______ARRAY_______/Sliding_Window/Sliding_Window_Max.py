
from collections import dequeu 

class Solution:
    # t: O(N), s: O(N)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        # Q[0] will have the max value, and it will be monothonically decreasing queue. 
        Q = deque() # index (index of numbers in nums)
        
        l = 0
        for r in range(len(nums)):
            # pop smaller values from the tail of the queue
            while Q and nums[Q[-1]] < nums[r]:
                Q.pop()
            
            Q.append(r)
            
            # if we are sure to extend the window to its size (initial edge case)
            # l ptr should only be increamented if we were extend the window to k size. 
            if  r - l + 1 >= k: # k'th index is k-1 in array
                output.append(nums[Q[0]]) # add max which located at the head of the queue. 
                l += 1 # shring the window with l
                if l > Q[0]:
                    Q.popleft()
        
        return output
            

