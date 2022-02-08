// https://leetcode.com/problems/product-of-array-except-self/

// time complexity: O(N)
// space complexity: O(1) // Problem states that, using the answer array does not add aditional space complexity.
class Product_Of_Array_Except_Self {
    
    // time complexity: O(N)
    // space complexity: O(N)
    public int[] productExceptSelf2(int[] nums) {
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
            right[j] = right[j+1] * nums[j+1];
        }
        
        for(int i = 0; i < length; i++) {
            answer[i] = left[i] * right[i];
        }
        
        return answer;
        
    }

    // Optimized!
    // time complexity: O(N)
    // space complexity: O(1)
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        
        int[] answer = new int[length];
        
        answer[0] = 1;
        for(int i = 1; i < length; i++) {
            answer[i] = answer[i-1] * nums[i-1];
        }
        
        int R = 1;
        for(int i = length-1; i >= 0; i--) {
            answer[i] = answer[i] * R;
            R *= nums[i]
        }

        return answer;
    }
}

/* Note:
    First of all, using the answer array, ans[0] = 1, for(int i = 1 then ...) leftProduct with answer[i] = nums[i-1] * ans[i-1]
    Secondly, starting from R =0, then for(int i = nums.length-1...) then answer[i] = answer[i] * R and R = R * nums[i]; 
*/