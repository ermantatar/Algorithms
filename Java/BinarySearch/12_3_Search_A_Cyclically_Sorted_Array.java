
// [378][478][550][631][103][203][220][234][279][368]

/*
for any m, if A[m] > A[n - 1], then the minimum value must be an index in the range [m + 1, n —1]. 
Conversely, if A[m] < A[n - 1], then no index in the range [m + 1, n —1] can be the index of the minimum value. 
(The minimum value may be at A[m].) Note that it is not possible for A[m] = A[n - 1], 
since it is given that all elements are distinct. 
These two observations are the basis for a binary search algorithm, described below.
*/

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