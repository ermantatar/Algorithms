class Solution:
    # t: O(|V|)
    # s: O(|V|)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # edge cases 
        if n <= 2:
            return [i for i in range(n)]
        
        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        # initialize the first layer of leaves (has one connection to inner zone)
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2: 
            
            remaining_nodes -= len(leaves)
            new_leaves = []
            
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            #prepare for the next round
            leaves = new_leaves
        
        # remaining nodes are the centroids of the graph. 
        return leaves 

# Look at this one too, as a base to this question
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/