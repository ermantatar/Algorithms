class MedianFinder {
    
    private static final int DEFAULT_INITIAL_CAPACITY = 16;
    PriorityQueue<Integer> minHeap;
    PriorityQueue<Integer> maxHeap;
    
    public MedianFinder() {
        
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>(DEFAULT_INITIAL_CAPACITY, Collections.reverseOrder());
        
    }
    
    public void addNum(int num) {
        if (this.minHeap.isEmpty()) {
            minHeap.add(num);
        } else {
            if ( num >= this.minHeap.peek()) {
                this.minHeap.add(num);
            } else {
                this.maxHeap.add(num);
            }
        }
        
        if (this.minHeap.size() > this.maxHeap.size() + 1) {
            this.maxHeap.add(this.minHeap.remove());
        } else if (this.maxHeap.size() > this.minHeap.size()) {
            this.minHeap.add(this.maxHeap.remove());
        }
    }
    
    public double findMedian() {
        return minHeap.size() == maxHeap.size() ? 0.5 * (maxHeap.peek() + minHeap.peek()) : minHeap.peek();   
    }
}

// time complexity is O(LogN)
// Space is O(N)


/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */