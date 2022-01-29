// Input Array is sorted this time, and return 1-indexed result.
// t: O(N)
// s: O(1)
class Solution {
    public int[] twoSumII(int[] nummbers, int target) {
        int left = 0;
        int right = nummbers.length - 1;

        while (left < right) {
            int sum = nummbers[left] + nummbers[right];

            if (sum == target) {
                return int[]{left + 1, right + 1};
            } else if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            }
        }

        return int[]{-1, -1}; // There is no pair exist! 
    }
}