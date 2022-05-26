class Solution {
    public static boolean isTextSubstringOfMagazine(String letterText, String magazine) {
        Map<Character, Integer> charFrequencyForLetter = new HashMap<>();
        // compute the frequency for the letter characters
        for(int i = 0; i < letterText.length(); i++) {
            char c = letterText.charAt(i);
            if (!charFrequencyForLetter.containsKey(c)) {
                charFrequencyForLetter.put(c, 1);
            } else {
                charFrequencyForLetter.put(c, charFrequencyForLetter.get(c) + 1)
            }
            // charFrequencyForLetter.put(c, charFrequencyForLetter.getOrDefault(c, 0) + 1);

            // Now, let's check if magazine characters includes all letterText characters.
            for(char c : magazine.toCharArray()) {
                if (charFrequencyForLetter.containsKey(c)) {
                    charFrequencyForLetter.put(c, charFrequencyForLetter.get(c) - 1);
                    if (charFrequencyForLetter.get(c) == 0) {
                        charFrequencyForLetter.remove(c);
                        if (charFrequencyForLetter.isEmpty()) {
                            break;
                        }
                    }
                }
            }

            return charFrequencyForLetter.isEmpty();
        }
    }
}

// The worst case, we need to iterate all characters in the letterText and magazine so it would be O(m + n)
// Space complexity is O(L) which is the number of unique characters in the string.