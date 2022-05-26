class Solution:
    # Approach: Kruskal Algorithm utilizing UnionFind Data Structure. 
    # t: O(ElogE)
    # s: O(E)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        all_edges = []
        
        #storing all edges of our complete graph 
        for curr_node in range(n):
            for next_node in range(curr_node+1, n):
                edge_weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                all_edges.append([edge_weight, curr_node, next_node])
        
        #sort all edges for Kruskal algorithm 
        all_edges.sort(key= lambda x: x[0])
        
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        
        for weight, node1, node2 in all_edges:
            if uf.union(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n-1:
                    break
        
        return mst_cost
        


class UnionFind:
    # t: O(N)
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    # t: O(α(N))
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    

    # The union function with union by rank
    # t: O(α(N))
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if self.connected(x, y): return False
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        return True
    # t: O(α(N))
    def connected(self, x, y):
        return self.find(x) == self.find(y)

### Leetcode Graph Card Kruskal - Solution ### 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        uf = UnionFind(size)

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                # Calculate the distance between two coordinates.
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                pq.append(edge)
        
        # Convert pq into a heap.
        heapq.heapify(pq)

        result = 0
        count = size - 1
        while pq and count > 0:
            edge = heapq.heappop(pq)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                result += edge.cost
                count -= 1
        return result

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()
    print(f"points = {points}")
    print(f"Minimum Cost to Connect Points = {solution.minCostConnectPoints(points)}")



''' Prim's Algorithm '''

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost 

class Solution:
	def minCostConnectPoints(self, points: List[List[int]]) -> int:
		
		if not points or len(points) == 0:
			return 0
		
		size = len(points)
		pq = []
		visited = [False] * size
		result = 0
		vertex_count = size - 1
		
		# add all edges from points[0] vertexs 
		x1, y1 = points[0]
		for i in range(1, size):
			# calculate the distance 
			x2, y2 = points[i]
			cost = abs(x1-  x2) + abs(y1 - y2) 
			edge = Edge(cost, 0, j)
			pq.append(edge)
		
		# Convert pq to a heap.
		heapq.heapify(pq)

		visited[0] = True
		while pq and vertex_count > 0:
			edge = heapq.heappop(pq)
			cost = edge.cost
			point1 = edge.point1
			point2 = edge.point2
			
			if not visited[point2]:
				result += cost 
				visited[point2] = True
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0]-points[j][0]) +\
                                    abs(points[point2][1]-points[j][1])
                        
                        heapq.heappush(pq, Edge(distance, point2, j))
                vertex_count -1 

                                    