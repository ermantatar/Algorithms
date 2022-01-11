/*
https://leetcode.com/explore/featured/card/graph/619/depth-first-search-in-graph/3849/

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
*/

class DFS_Solution {
    // DFS
    public List<List<Integer>> allPathSourceTarget(int[][] graph) {
        
        List<List<Integer>> paths = new ArrayList<>();
        if (graph == null || graph.length == 0) {
            return paths;
        }

        dfs(graph, 0, new ArrayList<>(), paths);
        return paths;
    }

    void dfs(int[][] graph, int node, List<Integer> path, List<List<Integer>> paths) {

        path.add(0);
        if (node == graph.length - 1) {
            paths.add(new ArrayList<>(path));
            return;
        }

        for(int nextNode : graph[node]) {
            dfs(graph, nextNode, path, paths);
            path.remove(path.size()-1);
        }
    }
}

// t: O(2^V * V)
// s: O(V)


// BigO
// t: O(2^V) * O(V)
// s: O(2^V) * O(V)
class BFS_Solution {
    public List<List<Integer>> allPathSourceTarget(int[][] graph) {
        List<List<Integer>> paths = new ArrayList<>();

        if (graph == null || graph.length == 0) {
            return paths;
        }

        Queue<List<Integer>> queue = new LinkedList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        queue.add(path);

        while(!queue.isEmpty()) {
            List<Integer> currentPath = queue.poll();
            int node = currentPath.get(currentPath.size() - 1); // [0, 1] means link goes 0 to 1
            for(int nextNode : graph[node]) {
                List<Integer> newPath = new ArrayList<>(currentPath);
                newPath.add(nextNode);
                if (nextNode == graph.length-1) {
                    paths.add(new ArrayList<>(newPath));
                } else {
                    queue.add(new ArrayList<>(newPath));
                }
            }
        }

        return paths;
    }
}