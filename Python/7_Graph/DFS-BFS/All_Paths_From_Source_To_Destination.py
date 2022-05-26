class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph, seen = defaultdict(list), set()

        for fr, to in edges:
            graph[fr].append(to)

        if not graph or source not in graph:
            return source == destination 

        # if we hit a dead end, return true if it's the destination
        # if we've seen the node return false 
        # otherwise return true 
        def dfs(node, destination, graph, seen):
            if node == destination and len(graph[node])==0:     # To prevent cycles.
                return True
            elif len(graph[node]) == 0:
                return False
            else:
                seen.add(node)
                for neighbor in graph[node]:
                    if neighbor == node or neighbor in seen or not dfs(neighbor, destination, graph, seen):
                        return False 
                seen.discard(node)
                return True 
                
        return dfs(source, destination, graph, seen)
