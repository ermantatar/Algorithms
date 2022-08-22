class UnionFind:
    # t: O(a(N)), s: O(N)
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
                return True 
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind(len(edges)+1)
        
        for v1, v2 in edges:
            if uf.isConnected(v1, v2):
                return [v1, v2]
            else:
                uf.union(v1, v2)