class Container_With_Most_Water {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        
        while(left <= right) {
            
            int currentArea = (right - left) * Math.min(height[left], height[right]);
            
            maxArea = Math.max(maxArea, currentArea);
            
            if (height[right] > height[left]) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxArea;
    }
}

// Time complexity: O(N) Single pass. 
// Space Complexity: O(1) Constant space is used. 
