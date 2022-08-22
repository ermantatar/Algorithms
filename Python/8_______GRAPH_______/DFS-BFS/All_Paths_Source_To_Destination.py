class Solution:
    # t, s: O(|V| + |E|)
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        graph = collections.defaultdict(list)
        seen = set()
        
        for fr, to in edges:
            graph[fr].append(to)
        
        if graph[destination]:
            return False 
        
        def dfs(node):
            
            # there could be many sink nodes that are not destination
            if len(graph[node]) == 0:
                return node == destination
            
            for nxt in graph[node]:
                # cycle check! 
                if nxt in seen:
                    return False 
                
                seen.add(nxt)
                
                if not dfs(nxt):
                    return False 
                
                seen.remove(nxt)
            
            # congrats all paths lead to destination
            return True 
            
        seen.add(source)
        return dfs(source)