
import heapq 



def findTheSecondLargest(nums, k = 2):
    
    if not nums:
        return -1 
    
    heap = []

    heapq.heapify(heap)

    # built the heap
    for num in nums:
        heapq.heappush(heap, -num)
    
    res = 0
    for _ in range(k):
        res = heapq.heappop(heap) 

    return -res 


findTheSecondLargest([-1, -2, -3, -4], 2)


print(findTheSecondLargest([3,5,2,1,7,9,8], 2)) 

assert findTheSecondLargest([3,5,2,1,7,9,8], 2) == 8

assert findTheSecondLargest([1,5,2,1,5], 2) == 5

assert findTheSecondLargest([], 2) == -1

print(findTheSecondLargest([-1, -2, -3, -4], 2))

[9, 8] < 8

x