class Solution:
    # Dijkstra1
    # t: O(E + VlogV)
    # s: O(V + E)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        queue, dist, adj = [(0, k)], {}, collections.defaultdict(list)
        
        for u, v, w in times:
            adj[u].append((w, v))
        
        while queue:
            time, node = heapq.heappop(queue)
            if not node in dist:
                dist[node] = time
                
                for w, v in adj[node]:
                    heapq.heappush(queue, (dist[node]+w, v))
            
            if len(dist) == n:
                return time 
        
        return -1 

    # Dijkstra2
    # t: O(E + VlogV)
    # s: O(V + E)
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w
        heap = [(0, K)]
        dist = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        
        return max(dist.values()) if len(dist) == N else -1

# This question has Bellman-Ford, Dijkstra, SPFA, Floyd Warshall Algorithms
# https://leetcode.com/problems/network-delay-time/discuss/283711/Python-Bellman-Ford-SPFA-Dijkstra-Floyd-clean-and-easy-to-understand