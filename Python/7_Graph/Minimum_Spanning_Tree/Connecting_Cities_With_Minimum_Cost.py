''' Kruskal Algorith '''
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if self.isConnected(x, y):
            return False 
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.root[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        return True 
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
    def amountOfRoot(self):
        total_count = 0
        for i in range(1, len(self.root)):
            if i == self.root[i]:
                total_count += 1
        return total_count
    
class Solution:
    # t: O(|E|log|E|)
    # s: O(|V|)
    def minimumCost(self, n: int, connections):
        if not connections or len(connections) == 0:
            return 0
        
        connections.sort(key = lambda x: x[2])
        
        uf = UnionFind(n+1)
        total_edge_used = 0 # N-1 edge is the max expected. 
        total_cost = 0
        for v1, v2, cost in connections:
            if uf.union(v1, v2):
                
                total_cost += cost
                total_edge_used += 1
                if total_edge_used == n-1:
                    break
        
        if uf.amountOfRoot() != 1:
            return -1
        else:
            return total_cost



''' Prim's Algorithm '''
'''Connecting Cities with Minimum Cost == Find Minimum Spanning Tree'''
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        '''
        Prim's Algorithm:
        1) Initialize a tree with a single vertex, chosen
        arbitrarily from the graph.
        2) Grow the tree by one edge: of the edges that
        connect the tree to vertices not yet in the tree,
        find the minimum-weight edge, and transfer it to the tree.
        3) Repeat step 2 (until all vertices are in the tree).
        '''
        # city1 <-> city2 may have multiple different cost connections,
        # so use a list of tuples. Nested dict will break algorithm.
        G = collections.defaultdict(list)
        for city1, city2, cost in connections:
            G[city1].append((cost, city2))
            G[city2].append((cost, city1))
        
        queue = [(0, N)]  # [1] Arbitrary starting point N costs 0.
        visited = set()
        total = 0
        while queue and len(visited) < N: # [3] Exit if all cities are visited.
            # cost is always least cost connection in queue.
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost # [2] Grow tree by one edge.
                for edge_cost, next_city in G[city]:
                    heapq.heappush(queue, (edge_cost, next_city))
        return total if len(visited) == N else -1