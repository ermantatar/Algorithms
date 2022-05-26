/*
    Note: 
    * Check if(nums[mid] == target) return nums[mid];
    * Check rotation with main two else if - else if 
    * Check with mid, and left, main opt1 -> nums[left] < nums[mid], 
    * there is sorted sequence and if target inside the border?
    * similarly check other if else main opt2 -> nums[left] >= nums[mid] 
*/

// t: O(logN)
// s: O(1)

class Solution {
    public int search(int[] nums, int target) {
        
        if( nums.length == 1 && nums[0] != target) return -1;

        int left = 0, right = nums.length - 1;

        while(left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[left] < nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if (nums[left] >= nums[mid]) {
                if (nums[mid] <= target && target < nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
}