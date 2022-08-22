from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self, x, y):
        
        rootX = self.find(x)
        rootY = self.find(y)
        
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

# Let E be the number of edges, and N is the number of Nodes, worst case is,  |E| - 1 = |N|, otherwise return False  
# t: O(N * a(N))
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # In order to be tree, there should not be cycles, so edge count should be equal to |E| = |V| - 1
        if len(edges) != n-1:
            return False
        
        uf = UnionFind(n)
        for v1, v2 in edges:
            if uf.isConnected(v1, v2):
                return False 
            else:
                uf.union(v1, v2)
        
        return True

