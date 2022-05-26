class Solution {
    private static final int DEFAULT_INITIAL_CAPACITY = 16;

    public static void onlineMedian(Iterator<Integer> sequence) {
        // minHeap stores the larger half seen so far.
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        // maxHeap stores the smaller half seen so far.
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(
            DEFAULT_INITIAL_CAPACITY, Collection.reverseOrder()
        );

        while(sequence.hasNext()) {
            int x = sequence.next();

            if (minHeap.isEmpty()) {
                // this is the very first element.
                minHeap.add(x);
            } else {
                if (x >= minHeap.peek()) {
                    minHeap.add(x);
                } else {
                    maxHeap.add(x);
                }
            }
        }

        // Ensure minHeap and maxHeap have equal amount of elements 
        // if even number of elements has seen so far.
        // otherwise, minHeap should have +1
        if (minHeap.size() > maxHeap.size() + 1) {
            maxHeap.add(minHeap.remove());
        } else if (maxHeap.size() > minHeap.size()) {
            minHeap.add(maxHeap.remove());
        }

        System.out.println(minHeap.size() == maxHeap.size() ? 0.5 * (maxHeap.peek() + minHeap.peek()) : minHeap.peek());
    }
}

// time complexity is O(LogN)
// Space is O(N)

/*
1. Read in 1: L=[1],H=[],medianis1.
2. Read in 0: L=[1],H=[0],medianis(1+0)/2=0.5.
3. Read in 3: L=[1,3],H=[0],medianis1.
4. Read in 5: L=[3,5],H=[1,0],medianis(3+l)/2=2.
5. Read in 2: L=[2,3,5],H=[1,0],medianis2.
6. Read in 0: L=[2,3,5],H=[1,0,0],medianis(2+l)/2=1.5. 7. Readin1:L=[1,2,3,5],H=[1,0,0],medianis1.
*/