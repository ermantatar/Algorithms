from ast import List

class Solution:
    # t: O(N)
    # s: O(1)
    def maxWater(self, height: List[int]) -> int:
        l, r, maxArea = 0, len(height)-1, 0

        while l <= r:

            currentArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, currentArea)
            
            if (height[r] > height[l]):
                l+=1
            else:
                r-=1

        return maxArea
    
    '''
    - Calculate the area as you move pointers, L -> ... <- R
    - Keep local maximum with max_so_far = max(max_so_far, curent_area)
    - Move the shorter pointer, (height[R] > height[L]) L += 1 or R-= 1
    '''
    
    

        