class Solution {
    public static void mergeTwoSortedArrays(List<Integer> A, int Asize, List<Integer> B, int Bsize) {
        int idx_A = Asize - 1;
        int idx_B = Bsize - 1;
        int writeIndex = Asize + Bsize - 1;

        while(idx_A >= 0 && idx_B >= 0) {
            A.set(writeIndex--, A.get(idx_A) > B.get(idx_B) ? A.get(idx_A--) : B.get(idx_B--));
        }

        // because, we are already iterating over the A, then A, is done, if B is done. 
        // If B is longer than A, then 
        while(idx_B >= 0) {
            A.set(writeIndex--, B.get(idx_B--))
        }
    }
}

// Leetcode Solution
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int idx_1 = m - 1;
        int idx_2 = n - 1;
        int writeIndex = m + n - 1;

        while(idx_1 >= 0 && idx_2 >= 0) {
            nums1[writeIndex--] = nums1[idx_1] > nums2[idx_2] ? nums1[idx_1--] : nums2[idx_2--];
        }

        // because, we are already iterating over the A, then A, is done, if B is done. 
        // If B is longer than A, then 
        while(idx_2 >= 0) {
            nums1[writeIndex--] = nums2[idx_2--];
        }
    }
}