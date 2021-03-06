// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Longest_Substring_Without_Repeating_Characters {
    class Brute_Force_Solution {
        // Time Complexity: O(N^3)
        // Space Complexity: O(M)
        public int lengthOfLongestSubstringWithoutRepeatingCharacters(String str) { 
        
            int res = 0;
            
            for(int i = 0; i < str.length(); i++) {
                for (int j = i; j < str.length(); j++) {
                    if (checkRepetition(str, i, j)) {
                        res = Math.max(res, j-i+1);
                    }
                }
            }
            
            return res;
        }

        public boolean checkRepetition(String str, int start, int end) {
            int[] chars = new int[128]; // This will cover all the consists of English letters, digits, symbols and spaces.

            while(start <= end) {
                
                char c = str.charAt(start);
                chars[c]++;
                if (chars[c] > 1) {
                    return false;
                }
                start++;
            }

            return true;
        }
    }

    // Sliding Window Approach
    // Time complexity : O(2N) = O(N)
    // Space complexity : O(min(m, n)), Size of the string, or the charset. 
    class SlidingWindow_Solution {
        public int lengthOfLongestSubstringWithoutRepeatingCharacters(String s) {
            int[] chars = new int[128];

            int left = 0;
            int right = 0;
            int res = 0;

            while (right < s.length()) {

                char r = s.charAt(right);
                chars[r]++;

                while(chars[r] > 1) {
                    char l = s.charAt(left);
                    chars[l]--;
                    left++;
                }
                

                res = Math.max(res, right - left + 1);
                right++;
            }

            return res;
        }
    }

    // Optimized Sliding Window Approach
    // Time complexity : O(N) = O(N)
    // Space complexity : O(min(m, n)), Size of the string, or the charset.

    /*
        Optimized Sliding Window approach. 
        Create R, L, Len variables set to 0.
        While R is traverse the string, check if current char is in map. 
        If so, make sure if it's index position is greater or equal to L. 
        If so, move the L, current char index + 1
        In every loop, make sure, you add current char and its index to map
        Check max len for the current round, Math.max(len, R - L + 1)
        Increase the R with +1
    */ 

    class SlidingWindowOptimized_Solution {
        public int lengthOfLongestSubstringWithoutRepeatingCharacters(String s) {

            Map<Character, Integer> map = new HashMap<>();
            int L = 0, R = 0, len = 0;

            while(R < s.length()) {

                char c = s.charAt(R);

                if (map.containsKey(c)) {
                    if (map.get(c) >= L) {
                        L = map.get(c) + 1;
                    }
                }

                map.put(c, R);
                len = Math.max(len, R - L + 1);
                
                R++;
            }
            
            return len; 
        }
    }

}
