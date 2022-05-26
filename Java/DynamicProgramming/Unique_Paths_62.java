// Not fast enough to pass all the test cases, but idea is, 
// think about last cell, how to reach there? from the (m-1, n) or (m, n-1)
// there is no 3rd option, so let the calculate for those cells, it is a recursion. 

class Solution {
    public int uniquePaths(int m, int n) {
        
        if ( m == 1 || n == 1) {
            return 1;
        }
        
        return uniquePaths(m-1, n) + uniquePaths(m, n-1);
    }
}

// Dynamic Programming Version of Recursion Solution
// technique is, reach the cell from the total count of previous cell jumps possibilites.
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        for(int[] arr : dp) {
            Arrays.fill(arr, 1);
        }
        
        for(int row = 1; row < m; row++) {
            for(int col = 1; col < n; col++) {
                dp[row][col] = dp[row-1][col] + dp[row][col-1];
            }
        }
        
        return dp[m-1][n-1];
    }
}

// time complexity: O(n)xO(m)
// space complexity: O(n)xO(m)
