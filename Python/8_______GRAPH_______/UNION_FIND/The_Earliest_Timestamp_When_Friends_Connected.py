class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        is_merged = False
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            is_merged = True
            
        return is_merged
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        # First, we need to sort the events in chronological order.
        logs.sort(key = lambda x: x[0])
        
        uf = UnionFind(n)
        
        group_count = n
        
        # We merge the groups along the way 
        for timestamp, friend_a, friend_b in logs:
            if uf.union(friend_a, friend_b):
                group_count -= 1
            
            if group_count == 1:
                return timestamp
            
        # There are still more than one groups left,
        #  i.e. not everyone is connected.
        
        return -1
        