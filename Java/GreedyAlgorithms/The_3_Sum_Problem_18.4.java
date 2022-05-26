import java.util.List;
import java.util.Collection;

class The_3_Sum_Problem_18_4 {
    
    public static boolean hasThreeSum(List<Integer> A, int t) {
        
        Collection.sort(A);
        // Finds if the sum of two numbers in A equals to t - a.
        return A.stream().anyMatch(a -> hasTwoSum(A, t-a));

        // for (Integer a : A) {
        //     if (hasTwoSum(A, t-a)) {
        //         return true;
        //     }
        // }
    }

    public static boolean hasTwoSum(List<Integer> A, int t) {
        
        int str = 0, end = A.size()-1;
        while ( str <= end ) {
            if (A.get(str) + A.get(end) == t) {
                return true;
            } else if (A.get(str) + A.get(end) < t) {
                ++str;
            } else {
                --end;
            }
        }
        return false;
    }  
}

// Time Complexity: O(nlogn) is the forst, but O(n) * O(n) finding twoSum is O(n^2)
// Space Complexity: O(1)
