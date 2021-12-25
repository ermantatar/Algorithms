private static class Compare {
    private static class GreaterThan implements Comparator<Integer> {
        public int compare(Integer o1, Integer o2) {
            return (o1 > o2) ? (o1.equals(o2) ? 0 : 1) : -1;
        }
    }

    public static final GreaterThan GREATER_THAN = new GreaterThan();
}

// The numbering starts from one, i.e., if A = [3,1,-1,2] then
// findKthLargest(A, 1) returns 3, findKthLargest(A, 2) returns 2,
// findKthLargest(A, 3) returns 1, and findKthLargest(A, 4) returns -1.

class Solution {
    public static int findKthLargest(List<Integer> A, int k) {
        return findKth(A, k, Compare.GREATER_THAN);
    }

    public static int findKth(List<Integer> A, int k, Comparator<Integer> cmp) {
        int left = 0, right = A.size() - 1;
        Random r = new Random(0);

        while(left <= right) {
            // Generates a random integer in [left, right]
            int pivotIdx = r.nextInt(right - left + 1) + left;
            int newPivotIdx = partitionAroundPivot(left, right, pivotIdx, A, cmp);

            if (newPivotIdx == length - k) {
                return A.get(newPivotIdx);
            } else if (newPivotIdx < length - k) {
                left = newPivotIdx + 1;
            } else {
                right = newPivotIdx - 1;
            }
        }
    }
    // Keep the pivot value, and move that guy to all the way to right. 
    // Create a new order with using new pivot index and partition the array, then bring back to old pivot value into this new index.
    // return the index, where array partitioned. 
    // Video helps 
    // https://www.youtube.com/watch?v=XEmy13g1Qxc
    
    private static int partitionAroundPivot(int left, int right, int pivotIdx, List<Integer> A, Comparator<Integer> cmp) {
        
        int pivotValue = A.get(pivotIdx);
        int newPivotIdx = left;

        Collections.swap(A, pivotIdx, right);
        for(int i = left; i < right; i++) {
            if(cmp.compare(A.get(i), pivotValue) < 0) {
                Collections.swap(A, i, newPivotIdx++);
            }
        }
        Collections.swap(A, newPivotIdx, right);
        return newPivotIdx;
    }
}

// this performs O(N) for the average case, and O(N^2) for the worst case.



