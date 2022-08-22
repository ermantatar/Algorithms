class Solution:
    # t: O(N * idle time), we can literally go idle time for every tasks.
    # s: O(N)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time 
        
        # count tasks and their frequencies
        count = collections.Counter(tasks)
        # Negating cnt will help us to turn into maxHeap, in Python we only have minHeap
        # We want to priotize the most freq task first
        maxHeap = [ -cnt for cnt in count.values()]
        heapq.heapify(maxHeap) # Turn into heap data structure, it takes O(N) time to turn it.  
        # Cool down queue for that task 
        queue = deque() # pairs of [(-cnt, next_available_time)]
        
        # if either one is not empty, it means we tasks to process
        time = 0
        while maxHeap or queue:
            time += 1
            
            if maxHeap:
                # Since we negated before, we will +1 to say, we processed this. 
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    # current time + idle period, next available time
                    queue.append([cnt, time + n])
            
            # time to process top of the queue 
            if queue and queue[0][1] == time:
                # we only push the freq value to maxHeap 
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time