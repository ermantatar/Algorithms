class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Negate all stones at first
        stones = [-s for s in stones]
        
        # set heapify order
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone2 != stone1:
                heapq.heappush(stones, stone1 - stone2)
                
        # will be at the bottom, we added here in case of no stones left
        stones.append(0)
        return abs(stones[0])