# This approach is to optimize the quik union approach. It is possible to end up with a straign line
# tree where find() function might end up Big O(N), since it is a bottleneck in union(), we need to
# optimize this. 

class UnionFind:
    # t: O(N)
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    # t: O(LogN)
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        
        return x
    # t: O(LogN)
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
    # t: O(LogN)
    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true


