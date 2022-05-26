// How to understand if Graph is a Tree. 


/*
For the graph to be a valid tree, it must have exactly n - 1 edges. 
Any less, and it can't possibly be fully connected. Any more, and it has to contain cycles. 
Additionally, if the graph is fully connected and contains exactly n - 1 edges, 
it can't possibly contain a cycle, and therefore must be a tree!

Going by this definition, our algorithm needs to do the following:
Check whether or not there are n - 1 edges. If there's not, then return false.
Check whether or not the graph is fully connected. Return true if it is, false if otherwise.

Read the article for the solution, it is amazing! 
https://leetcode.com/problems/graph-valid-tree/solution/
*/

// Question 
/*
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true
*/

class Iterative_DFS_Solution {
    public boolean validTree(int n, int[][] edges) {

        if (edges.length != n-1) { return false; } // first condition for being a Tree.

        List<List<Integer>> adjacencyList = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<Integer>());
        }

        for (int[] edge : edges) {
            adjacencyList.add(edge[0]).add(edge[1]);
            adjacencyList.add(edge[1]).add(edge[0]);
        }

        Stack<Integer> stack = new Stack<>(); // DFS Data Structure. 
        Set<Integer> seen = new HashSet<>();
        stack.push(0);
        set.add(0);

        while(!stack.isEmpty()) {
            int node = stack.pop();
            for(int neighbour : adjacencyList.get(node)) {
                if (seen.contains(neighbour)) {
                    continue;
                } else {
                    seen.add(neighbour);
                    stack.push(neighbour);
                }
            }
        }

        return seen.size() == n; // second condition for being a Tree. 
    }
}

class Recursive_DFS_Solution {

    private List<List<Integer>> adjacencyList = new ArrayList<>();
    private Set<Integer> seen = new HashSet<>();

    public boolean isValidTree(int n, int[][] edges) {
        
        if (edges.length != n-1) return false;

        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }

        // Carry out depth first search. 
        dfs(0);

        return seen.size() == n;
    }

    public void dfs(int node) {
        if (seen.contains(node)) return;

        seen.add(node); // visit node

        // traverse neighbours
        for (int node : adjacencyList.get(node)) {
            dfs(neighbour);
        }
    }
}

class Iterative_BFS_Solution {
    public boolean isValidTree(int n, int[][] edges) {
        if ( edges.length != n-1) return false;

        List<List<Integer>> adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }

        for(int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }

        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> seen = new HashSet<>();
        queue.offer(0);
        seen.add(0);

        while(!queue.isEmpty()) {
            int node = queue.poll();
            for (int neighbour : adjacencyList.get(node)) {
                if (!seen.contain(neighbour)) {
                    seen.add(neighbour);
                    queue.offer(neighbour);
                }
            }
        }

        return seen.size() == n;
    }
}

// All 3 are the same! 
// t: O(N), because we require to n-1 == edge amount, then 0(N) is the main dominator, we iterate through all vertices, so, overall we traverse O(N) vertices. 
// s: (N)


// UNIONFIND DATA STRUCTURE! 
// t: O(N * a(N)), union depends on the find() function, and we are optimizing everyone's parent to be root. It is why it's a(N) Inverse Ackerman Func (max => 4)
// s: O(n)

// when we are comparing the UnionFind with other algos, treat find() function as if it is O(1)
class Solution {
    public boolean validTree(int n, int[][] edges) {
        
        // Condition 1: The graph must contain n - 1 edges.
        if (edges.length != n -1) { return false;}
        
        // Condition 2: The graph must contain a single connected component.
        // Create a new UnionFind object with n nodes. 
        UnionFind uf = new UnionFind(n);
        
        for (int[] edge : edges) {
            int A = edge[0];
            int B = edge[1];
            if (uf.isConnected(A, B)) {
                return false;
            } 
            uf.union(A, B);
        }
        
        
        return true;
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
        
        public boolean isConnected(int x, int y) {
            return find(x) == find(y);
        }
    }
}

