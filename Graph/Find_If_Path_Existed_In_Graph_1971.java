class DFS_Solution {
    
    Set<Integer> explored = new HashSet<>();
    Map<Integer, List<Integer>> neighbors = new HashMap<>();
    
    public boolean validPath(int n, int[][] edges, int start, int end) {
        
        for(int i = 0; i<n; i++) {
            neighbors.put(i, new ArrayList<Integer>());
        }
        
        for(int[] edge: edges) {
            neighbors.get(edge[0]).add(edge[1]);
            neighbors.get(edge[1]).add(edge[0]);
        }
        
        return dfs(start, end, neighbors);
    }
    
    private boolean dfs(int start, int end, Map<Integer, List<Integer>> neighbors)
    {
        if(start == end)
            return true;
        explored.add(start);
        for(int node: neighbors.get(start)) {
            if(!explored.contains(node)) {
                if (dfs(node, end, neighbors)) {
                    return true;
                }
            }
            explored.add(node);
        }
        return false;
    }
}


// t: O(V + E)
// s: O(V)

import java.util.*;
class Solution {
    
    public boolean validPath(int n, int[][] edges, int start, int end) {
        
        if (edges == null || edges.length == 0) {
            return true;
        }  
        
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
        
        queue.offer(start);
        seen.add(start);
        
        while(!queue.isEmpty()) {
            int node = queue.poll();
            for (int neighbour : adjacencyList.get(node)) {
                if (!seen.contains(neighbour)) {
                    if (neighbour == end) return true;
                    seen.add(neighbour);
                    queue.offer(neighbour);
                }
            }
        }
        
        return false;
    }
}