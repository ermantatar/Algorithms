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
        
        Map<Character, Integer> freqMap = new HashMap();
        int res = 0;
        int l = 0;
        int maxF = 0;

        for (int r = 0; r < s.length(); r++) {

            freqMap.put(s.charAt(r), freqMap.getOrDefault(s.charAt(r), 0) + 1);
            maxF = Math.max(maxF, freqMap.get(s.charAt(r)));

            if ((r-l+1) - maxF > k) {
                freqMap.put(s.charAt(l), freqMap.get(l) - 1);
                l++;
            }

            res = Math.max(res, r-l+1);
        }

        return res;
    }
}
/*

Math.max and Math.min only accept pairs of arguments. You can't pass more than 2 parameters.

The neatest way to do this would be to wrap the values into a List<Integer> and 

then use Collections.max and Collections.min

*/