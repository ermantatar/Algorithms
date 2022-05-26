// https://leetcode.com/problems/maximum-subarray/

class Maximum_Subarray {
    // Brute Force
    // Time Complexity: O(N^2)
    // Space Complexity: O(1)
    public int maxSubArray(int[] nums) {
        int maxSubarray = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int currentSubarray = 0;
            for (int j = i; j < nums.length; j++) {
                currentSubarray += nums[j];
                maxSubarray = Math.max(maxSubarray, currentSubarray);
            }
        }
        
        return maxSubarray;
    }

    // Time Complexity: O(N)
    // Space Complexity: O(1)
    public int maxSubArray(int[] nums) {
        
        int currentSubarray = Integer.MIN_VALUE;
        int maxSubarray = Integer.MIN_VALUE;
        
        for(int num : nums) {

            currentSubarray = Math.max(num, currentSubarray + num);
            maxSubarray = Math.max(maxSubarray, currentSubarray);
        }
        
        return maxSubarray;
    }

}

