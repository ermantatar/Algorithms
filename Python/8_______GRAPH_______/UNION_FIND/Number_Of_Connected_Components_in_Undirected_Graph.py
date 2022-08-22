class UnionFind:
    
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.rootAmount = 0
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.root[x]
        rootY = self.root[y]
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
    
    def countRoots(self):
        for i in range(len(self.root)):
            if i == self.root[i]:
                self.rootAmount += 1
        
        return self.rootAmount

class Solution:
    # t: O(N * a(N))
    # s: O(N)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        for v1, v2 in edges:
            if not uf.isConnected(v1, v2):
                uf.union(v1, v2)
        
        return uf.countRoots()
        