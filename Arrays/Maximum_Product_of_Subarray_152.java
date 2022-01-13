/*
    Algorithm behind it, 
    * initialize result, max_so_far, min_so_far = nums[0];
    * keep track of [max_so_far, min_so_far]
    * every round, Math.max or min(currentNum, max_so_far * currentNum, min_so_far * currentNum)
    * calculate ultimate max, result = Math.max(result, max_so_far)
*/

// t: O(N)
// s: O(1)

class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) return 0;
        
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];
        
        for(int i = 1; i < nums.length; i++) {
            // currrent number
            int curr = nums[i];
            
            // protect previous round 
            int prevMin = minSoFar;
            int prevMax = maxSoFar;
            
            // calculate new results
            maxSoFar = Math.max(curr, Math.max(curr* prevMax, curr * prevMin));
            minSoFar = Math.min(curr, Math.min(curr * prevMax, curr * prevMin));
            
            // calculate the result
            result = Math.max(maxSoFar, result);
        }
        
        return result;
    }
}