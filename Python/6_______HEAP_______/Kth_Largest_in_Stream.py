class KthLargest:
    # Construction will take t: O(NlogN)
    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Worst case, N time, LogN operation.
        while len(self.heap) > self.capacity:
            heapq.heappop(self.heap)
        
    # Every call, Log(k), if we call this function M times, O(MlogK)
    def add(self, val: int) -> int:
        # heap will take care of the position
        heapq.heappush(self.heap, val)
        # make sure after adding the new value, heap is not exceed its capacity. 
        if len(self.heap) > self.capacity:
            heapq.heappop(self.heap)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)