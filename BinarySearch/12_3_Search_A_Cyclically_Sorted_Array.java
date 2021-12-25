
// [378][478][550][631][103][203][220][234][279][368]

class Solution {
    public static int searchSmallest(List<Integer> A) {
        int left = 0;
        int right = A.size() - 1;

        while (left < right) {
            int mid = left + ((right - left) / 2);
            if (A.get(mid) > A.get(right)) {
                // minimum must be in A.sublist[mid+1, right+1]
                left = mid + 1;
            } else {
                // A.get(min) < A.get(right)
                // Minimum cannot be in A.sublist(mid + 1, right + 1), 
                // so it must be in A.sublist[left, mid+1]
                right = mid;
            }
        }
        // Loop ends when left == right
        return left;
    }
}

// time complexity is the same as binary search, O(LogN)

/*
Note that this problem cannot, in general, be solved in less than linear time when elements may be repeated. 
For example, if A consists of n - 1 Is and a single 0, that 0 cannot be detected in the worst-case without 
inspecting every element.
*/