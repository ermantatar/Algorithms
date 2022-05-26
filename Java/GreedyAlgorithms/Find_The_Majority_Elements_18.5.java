
/*
    (b,a,c,a,a,b,a,a,c,a)
    we will pick the b first, then we continue to iterate, 
    when we see the a, we will decrease the counter for the b, if it is 0, 
    then we will pick next item as a candidate, then the same process, we will see that 
    at the end, a will be the one with count more than 0. 
*/

public static String majoritySearch(Iterator<String> sequence) {
    String iter;
    String candidate;
    int candidateCount = 0;
    if (sequence.hasNext()) {
        iter = sequence.next();
        if (candidateCount == 0) {
            candidate = iter;
            candidateCount = 1;
        } else if (iter.equals(candidate)) {
            ++candidateCount;
        } else if (!iter.equals(candidate)) {
            --candidateCount;
        }
    }

    return candidate;
}

// time complexity: O(N)