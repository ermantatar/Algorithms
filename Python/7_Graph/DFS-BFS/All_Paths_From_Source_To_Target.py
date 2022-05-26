class Solution:
    #bfs
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        if not graph or len(graph) == 0:
            return paths

        queue = deque()
        path = [0]
        queue.append(path)

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            for next_node in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(next_node)

                if next_node == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        return paths

    #dfs 
    def allPathsSourceToTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return 
            
            for neighbor in graph[node]:
                dfs(neighbor)
                path.pop() # take out the target vertex. 

        paths = []
        path = []
        if not graph or len(graph) == 0:
            return paths 
        
        dfs(0)
        return paths