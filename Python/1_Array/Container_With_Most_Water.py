from ast import List


class Solution:
    def maxWater(self, height: List[int]) -> int:
        L, R, maxArea = 0, len(height), 0;

        while L <= R:

            currentArea = (R - L) * min(height[L], height[R])
            maxArea = max(maxArea, currentArea)
            
            if (height[R] > height[L]) {
                L+=;
            } else {
                R+=1;
            }

        return maxArea
    # t: O(N)
    # s: O(1)
    

        