// t: O(N)
// s: O(N)
class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()) return false;
        
        Map<Character, Integer> firstMap = new HashMap<>();
        
        for (Character c : s.toCharArray()) {
            firstMap.put(c, firstMap.getOrDefault(c, 0) + 1);
        }
        
        for (Character c : t.toCharArray()) {
            if (!firstMap.containsKey(c)) {
                return false;
            } else {
                firstMap.put(c, firstMap.get(c) - 1);
            }
        }
        
        for(Map.Entry<Character,Integer> entry : firstMap.entrySet()) {
            if (entry.getValue() != 0) {
                return false; 
            }
        }
        
        return true;
    }
}