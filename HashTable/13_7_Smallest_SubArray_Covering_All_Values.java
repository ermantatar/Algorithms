public static class Subarray {
    public Integer start;
    public Integer end;

    public Subarray(Integer start, Integer end) {
        this.start = start;
        this.end = end;
    }
}

class Solution {
    public static Subarray findSmallestSubarrayCoveringSet(List<String> paragraph, Set<String> keywords) {

        Map<String, Integer> keywordsToCover = new HashMap<>();
        for(String keyword : keywords) {
            keywordsToCover.put(keyword, keywordsToCover.containsKey(keyword) ? keywordsToCover.get(keyword) : 1);
        }

        Subarray result = new Subarray(-1, -1);
        int remainingToCover = keyword.size();

        for(int left = 0, right = 0; right < paragraph.size(); right++) {
            Integer keywordCount = keywordsToCover.get(paragraph.get(right));
            if (keywordCount != null) {
                keywordsToCover.put(paragraph.get(right), --keywordCount);
                if (keywordCount >= 0) {
                    --remainingToCover;
                }
            }

            // keeps advancing left until it reaches end or keywordsToCover does not have all keywords.
            while(remainingToCover == 0) {
                // first case, or there is a smaller sliding window 
                if ((result.start == -1 && result.end == -1) || right - left < result.end - result.start) {
                    result.start = left;
                    result.end = right;
                }

                keywordCount = keywordsToCover.get(paragraph.get(left));
                if (keywordCount != null) {
                    keywordsToCover.put(paragraph.get(left), ++keywordCount);
                    if (keywordCount > 0) {
                        ++remainingToCover;
                    }
                }
                ++left;
            }
        }
        return result; 
    }
}