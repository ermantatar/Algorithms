import java.util.Arrays;

public class Longest_Increasing_Subsequence {
    public int longestIncreasingSubsequence(int[] nums) {
        // base
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);

        for(int i = 1; i < nums.length; i++) {
            for(int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int longest = 0;
        for(int c : dp) {
            longest = Math.max(c, longest);
        }
        return longest;
    }
}
