class Solution:
    # t: O(N), s: O(1)
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            
            if leftMax < rightMax:
                # Inside of this scope, I already know, rightMax is higher, and I am limited by leftMax value
                l += 1
                leftMax = max(leftMax, height[l]) # making sure there will be no -water value. 
                res += leftMax - height[l]
            else:
                # Inside of this scope, I already know, leftMax is higher, and I am limited by rightMax value
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res 