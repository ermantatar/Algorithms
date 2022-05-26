// Brute Force 
class Solution {
    public static List<Integer> intersectTwoSortedArrays(List<Integer> A, List<Integer> B) {
        List<Integer> intersectionAB = new ArrayList<>();
        for (int i = 0; i < A.size(); i++) {
            if (i == 0 || A.get(i) != A.get(i-1)) {
                for (Integer b : B) {
                    if (A.get(i).equals(b)) {
                        intersectionAB.add(A.get(i));
                        break;
                    }
                }
            }
        }

        return intersectionAB;
    }
}
// time complexity: O(M) * O(N)

/*
Since both the arrays are sorted, we can make some optimizations. 
First, we can iterate through the first array and use binary search in array to test if the element is present in the second array.
*/
public static List<Integer> intersectTwoSortedArrays(List<Integer> A, List<Integer> B) {
    List<Integer> intersectionAB = new ArrayList<>();
    for(int i = 0; i < A.size(); i++) {
        if ((i == 0) || A.get(i) != A.get(i-1) && Collections.binarySearch(B, A.get(i)) >= 0) {
            intersectionAB.add(A.get(i));
        }
    }
    return intersectionAB;
}

// The time complexity is O(M * LogN)

// Optimization, to reduce the linear time. 

// Since we spend 0(1) time per input array element, the time complexity for the entire algorithm is 0(m + n).

public static List<Integer> intersectTwoSortedArrays(List<Integer> A, List<Integer> B) {
    List<Integer> intersectionAB = new ArrayList<>();

    int i = 0; 
    int j = 0;

    while (i < A.size() && j < B.size()) {
        if ((A.get(i) == B.get(j)) && (i == 0 || A.get(i) != A.get(i-1))) {
            intersectionAB.add(A.get(i));
            ++i;
            ++j;
        } else if (A.get(i) < B.get(j)) {
            i++;
        } else { // A.get(i) > B.get(j)
            ++j;
        }
    }

    return intersectionAB;
}



