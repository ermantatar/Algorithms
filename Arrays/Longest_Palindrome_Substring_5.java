class Solution {
    
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int oddPal = expandAroundCenter(s, i, i);
            int evenPal = expandAroundCenter(s, i, i+1); 
            int len = Math.max(oddPal, evenPal);
            
            if (len > end - start) {
                //rac[e]car, ith is e
                start = i - (len-1) / 2;
                end = i + len/2;
            }
        }
        
        return s.substring(start, end + 1);
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        int L = left, R = right;
        while(0 <= L && R < s.length() && s.charAt(L) == s.charAt(R)) {
            L--;
            R++;
        } 
        
        return R - L - 1;
    }
}

//time complexity: O(n^2)
//space complexity: O(1)