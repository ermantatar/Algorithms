class Solution {
    public int characterReplacement(String s, int k) {
        
        Map<Character, Integer> freqMap = new HashMap();
        int res = 0;
        int l = 0;
        int maxF = 0;

        for (int r = 0; r < s.length(); r++) {

            freqMap.put(s.charAt(r), freqMap.getOrDefault(s.charAt(r), 0) + 1);

            if ((r-l+1) - Collections.max(freqMap.values()) > k) {
                freqMap.put(s.charAt(l), freqMap.get(s.charAt(l)) - 1);
                l++;
            }


            res = Math.max(res, r-l+1);
        }

        return res;

    }
}

// We don't need to decrease the maxFrequency of the chars, since main formula is, 
// lengthOfWindow - maxFreqOfChars <= K

// So, we cannot consider the cases, where length of window is high but maxF of letter is low, 
// so we want them to be higher together, which is the where solution would be. 

class Optimized_Solution {
    public int longestRepeatingCharacterReplacement(String s, int k) {
        
        int R = 0, L = 0, len = 0, maxChar = 0;
        Map<Character, Integer> map = new HashMap();
        
        while(R < s.length()) {
            
            Character c = s.charAt(R);
            
            map.put(c, freqMap.getOrDefault(c, 0) + 1);
            
            maxChar = Math.max(maxChar, freqMap.get(c));
            
            if(R-L+1 - maxChar > k) {
                freqMap.put(s.charAt(L), freqMap.get(s.charAt(L)) - 1);
                L++;
            }
            
            len = Math.max(len, R-L+1);
            R++;
        }

        return len;
    }
}  
}
/*

Math.max and Math.min only accept pairs of arguments. You can't pass more than 2 parameters.

The neatest way to do this would be to wrap the values into a List<Integer> and 

then use Collections.max and Collections.min (Does not work with primitive types.)

*/