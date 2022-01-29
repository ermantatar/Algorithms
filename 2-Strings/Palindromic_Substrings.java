class Palindromic_Substring {
    
    public int countPalindromicSubstring(String s) {

        int ans = 0;

        for(int i = 0; i < s.length(); i++) {
            // Odd length palindromes
            ans += expandAroundCenter(s, i, i);
            
            // Even length palindromes
            ans += expandAroundCenter(s, i, i+1);
        }

        return ans;

    }

    private int expandAroundCenter(String s, int L, int R) {
        
        int ans = 0;

        while(0 <= L && R < s.length() && s.charAt(L) == s.charAt(R)) {
            L--;
            R++;
            ans++;
        }

        return ans;
    }
}

// t: O(N^2), imagine this as there are N center candidates, each center can extend n-1 times. 
// s: O(1)