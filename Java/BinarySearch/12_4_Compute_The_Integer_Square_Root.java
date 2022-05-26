// Find a integer, whose square is less than or equal to given k. 
// k = 26, then integer result = 5;
class Solution {
    public static int squareRoot(int k) {
        long left = 0, right = k;
        // Candidate interval [left, right] where everything before left has 
        // square <= k, and everything after right has square > k.
        while (left <= right) {
            long mid = left + ((right - left) / 2));
            long midSquared = mid * mid;
            if (midSquared <= k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return (int) left - 1;
    }
}
// In return statement, do not forget the corner case.
// For fc = 25, the sequence of intervals is [0,25],[0,11],[6,11],[6,7],[6,5], The re¬ turned value is 6 - 1 =5.

// time complexity is O(logK), K is equal to search interval
// space complexity O(1)