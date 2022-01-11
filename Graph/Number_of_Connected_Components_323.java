// t: O(E * α(n))
// s: O(V)
class UnionFind_Solution {
    public int countComponents(int n, int[][] edges) {
        
        // Condition 2: The graph must contain a single connected component.
        // Create a new UnionFind object with n nodes. 
        UnionFind uf = new UnionFind(n);
        
        for (int[] edge : edges) {
            int A = edge[0];
            int B = edge[1];
            uf.union(A, B);
        }
        
        
        return uf.getNumberOfRoots();
    }
    
    class UnionFind {
        private int[] root;
        private int[] rank;
        
        public UnionFind(int size) {
            root = new int[size];
            rank = new int[size];
            
            for (int i = 0; i < size; i++) {
                root[i] = i;
                rank[i] = 1;
            }
        }
        
        public int find(int x) {
            if (x == root[x]) {
                return x;
            }
            
            return root[x] = find(root[x]);
        }
        
        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            
            if (rootX != rootY) {
                if (rank[rootX] > rank[rootY]) {
                    root[rootY] = rootX;
                } else if (rank[rootY] > rank[rootX]) {
                    root[rootX] = rootY;
                } else {
                    root[rootY] = rootX;
                    rank[rootX] += 1;
                }
            }
        }
        
        public int getNumberOfRoots() {
            int count = 0;
            for (int i = 0; i < root.length; i++) {
                if (i == root[i]) {
                    count++;
                }
            }
            
            return count;
        }
        
        public boolean isConnected(int x, int y) {
            return find(x) == find(y);
        }
    }
}