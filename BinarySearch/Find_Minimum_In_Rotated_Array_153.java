/*
    Note: 
    * Take advantage of array being sorted, BINARY SEARCH! 
    * Do some adjustments, instead of nums[mid] == value, return mid, 
    * if (nums[mid] > nums[mid + 1]) return nums[mid+1]
    * if (nums[mid - 1] > nums[mid]) return nums[mid]
    * move right and left pointer to other side of the array
*/

// t : O(logN)
// s : O(1)

class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 1 || nums[0] < nums[nums.length - 1]) return nums[0];

        int left = 0, right = nums.length - 1;

        while (right > left) {

            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[mid+1]) {
                return nums[mid+1];
            }

            if (nums[mid-1] > nums[mid]) {
                return nums[mid];
            }

            if (nums[0] < nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
}