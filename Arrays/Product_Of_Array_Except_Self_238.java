// https://leetcode.com/problems/product-of-array-except-self/

// time complexity: O(N)
// space complexity: O(N)
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] answer = new int[length];
        
        int[] left = new int[left];
        int[] right = new int[right];
        
        left[0] = 1;
        for(int i = 1; i < length; i++) {
            left[i] = left[i-1] * nums[i-1];
        }
        
        right[length-1] = 1;
        for (int j = length-2; j >= 0; j--) {
            right[i] = right[i+1] * nums[i+1];
        }
        
        for(int i = 0; i < length; i++) {
            answer[i] = left[i] * right[i];
        }
        
        return answer;
        
    }
}

// time complexity: O(N)
// space complexity: O(1) // Problem states that, using the answer array does not add aditional space complexity.
class Optimized_Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        
        int[] answer = new int[length];
        
        answer[0] = 1;
        for(int i = 1; i < length; i++) {
            answer[i] = answer[i-1] * nums[i-1];
        }
        
        int R_sum = 1;
        for(int i = length-1; i >= 0; i--) {
            answer[i] = answer[i] * R_sum;
            R_sum *= nums[i]
        }

        return answer;
    }
}