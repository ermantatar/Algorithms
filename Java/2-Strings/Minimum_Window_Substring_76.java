class Solution {
    public int[] minimumWindowSubstring(String s, String t) {

        if (s.length() == 0 || t.length() == 0) {
            return "";
        }

        Map<Character, Integer> dictT = new HashMap<>();

        for(Character c : t.toCharArray()) {
            dictT.put(c, dictT.getOrDefault(c, 0) + 1);
        }

        int L = 0, R = 0;

        int formed = 0, required = dictT.size();

        Map<Character, Integer> windowDict = new HashMap<>();

        int[] answer = new int[]{-1, -1, -1};

        while(R < s.length()) {
            Character c = s.charAt(R);
            windowDict.put(c, windowDict.getOrDefault(c, 0) + 1);

            if (dictT.containsKey(c) &&  dictT.get(c) == windowDict.get(c)) {
                formed++;
            }

            // shrink window.
            while(L <= R && formed == required) {
                
                if(answer[0] == -1 || R-L+1 < answer[0]) {
                    answer[0] = R-L+1;
                    answer[1] = L;
                    answer[2] = R;
                }

                Character lc = s.charAt(L);
                windowDict.put(lc, windowDict.get(lc) - 1);
                if (dictT.containsKey(c) &&  dictT.get(c) > windowDict.get(c)) {
                    formed--;
                }

                L++;
            }

            R++;
        }

        return answer[0] == -1 ? "" : s.substring(answer[2] - answer[1] + 1);
    }
}