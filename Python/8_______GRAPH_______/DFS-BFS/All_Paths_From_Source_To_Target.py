class Solution:
    # dfs
    # Time: O(2^n) Space: O(2^n)
    # This is a DAG graph, no need to use seen set, since there won't be cycle in DAG. 
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        output = []
        if not graph:
            return output
        
        
        def dfs(node, path):
            if node == len(graph)-1:
                output.append(path)
            
            for nxt in graph[node]:
                dfs(nxt, path + [nxt])
        
        path = [0]
        dfs(0, path)
        return output
    
    #BFS-DFS (just change the pop function in the queue)
    # Time: O(n * 2^n) Space: O(n * 2^n)
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        if not graph:
            return output

        queue = deque([[0],])

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            for nxt in graph[node]:
                new_path = current_path.copy()
                new_path.append(nxt)

                if nxt == len(graph) - 1:
                    output.append(new_path)
                else:
                    queue.append(new_path)
        return output