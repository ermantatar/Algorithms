class Solution:

    import heapq
    # Create a counter, and count the items and their frequency dictionary
    # Create an heap, and push all (count, num), if len(heap) > k: then pop()
    # Add all items in the heap to an result array, and return it.
    # T: O(Nlogk)if k < N and O(N) in the particular case k = N.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        result = []
        for n in nums:
            count = counter.get(n, 0) + 1
            counter[n] = count
        
        heap = []
        for num, count in counter.items():
            ele = (count, num)
            heapq.heappush(heap, ele)
            if len(heap) > k:
                heapq.heappop(heap)
        result = [x[1] for x in heap]
        return result
    # t: O(N), s: O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]
        number_count = collections.defaultdict(int)
        for num in nums:
            number_count[num] += 1
            
        for num, freq in number_count.items():
            buckets[freq].append(num)
        
        # buckets is a double array
        flat_list = []
        # traverse from right to left so number with higher frequency come first
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    flat_list.append(num)
        return flat_list[:k]



from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        count_map = Counter(nums)
        
        return heapq.nlargest(k, count_map.keys(), key=count_map.get)



# This is a bucket sort problem. Read more about it. 
