/*
    Goal is to create this hashmap, then turn values into an arraylist. 
    
    {
        "aer" : ["are", "ear", "era"],
        "abt" : ["bat", "tab"],
        "ecdo": ["code"]
    }
*/

// time complexity: O(N * KlogK) | N is the strs array size, K is the maximum length of string inside of strs array.  
// space complexity: O(NK)

class First_Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList();
        
        Map<String, List<String>> ans = new HashMap<String, List<String>>();
        
        for (String s : strs) {
            
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = String.valueOf(ca);
            
            if (!ans.containsKey(key)) {
                ans.put(key, new ArrayList());
            } 
            
            ans.get(key).add(s);
        }
        return new ArrayList(ans.values());
    }
}

// time complexity: O(NK) | N is the strs array size, K is the maximum length of string inside of strs array.  
// space complexity: O(NK)
class Optimal_Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList();
        
        Map<String, List<String>> ans = new HashMap<String, List<String>>();
        int[] count = new int[26];
        
        for (String s : strs) {
            Arrays.fill(count, 0);
            
            for(char c : s.toCharArray()) count[c - 'a']++;
            
            StringBuilder sb = new StringBuilder("");
            for(int i = 0; i < 26; i++) {
                sb.append("#");
                sb.append(count[i]);
            }
            String key = sb.toString();
            
            if (!ans.containsKey(key)) ans.put(key, new ArrayList());
            ans.get(key).add(s);
        }
        
        return new ArrayList(ans.values());
    }
}