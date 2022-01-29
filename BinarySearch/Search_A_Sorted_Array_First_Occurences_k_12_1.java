class Solution {
    public static int searchFirstOfK(List<Integer> A, int k) { 
        int left = 0, right = A.size() - 1, result = -1;

        while(left <= right) {
            int mid = left + ((right - left) / 2);
            if(A.get(mid) > k) {
                right = mid - 1;
            } else if (A.get(mid) == k) {
                result = mid;
                // we should see if there is a first occurence in the left side.
                // we are not interested, indexed bigger than index mid, since mid will be prior to them.
                right = mid - 1; 
            } else { // A.get(mid) < k
                left = mid + 1;
            }
        }

        return result;
    }
}

// time complexity: O(LogN)
// space complexity: O(1)