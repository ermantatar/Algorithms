class Solution:
    """
    N: Length of points
    t: O(Nlogk)
    s: O(N)
    
    Algorithm: We are looking for k closest point from the origin.
    This is perfect case for priority queue, calculate dist for all x, y
    Let the distance be the measurement Priority Queue will use to prioritize
    Pop, k times from the Priority Queue, those will be the closest ones. 
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y-0) ** 2)
            pts.append([dist, x, y])
        
        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        
        return res