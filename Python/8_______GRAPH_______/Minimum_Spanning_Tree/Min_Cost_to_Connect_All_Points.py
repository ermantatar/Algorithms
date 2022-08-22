class Solution:
    # Approach: Kruskal Algorithm utilizing UnionFind Data Structure.
    """
    Given array of points, return min cost to connect all points
    All points have 1 path b/w them, cost is Manhattan distance

    MST problem, Prim's, greedily pick node not in MST & has smallest edge cost
    Add to MST, & for all its neighbors, try to update min dist values, repeat

    Time: O(V^2) - t: O(ElogE)
    Space: O(V) - O(E)
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        all_edges = [] # [dist, v1, v2]
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                # calculate the distance
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                all_edges.append([dist, i, j])
        
        all_edges.sort(key = lambda x: x[0])
        
        uf = UnionFind(len(points))
        mst_cost = 0
        edge_used = 0
        
        for dist, v1, v2 in all_edges:
            if uf.isConnected(v1, v2) == False:
                uf.union(v1, v2)
                mst_cost += dist
                edge_used += 1
                if edge_used == len(points)-1:
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

                                    