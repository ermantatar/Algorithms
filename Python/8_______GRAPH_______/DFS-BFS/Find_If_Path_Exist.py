from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjacency_list = defaultdict(list)

        for v1, v2 in edges:
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)
        
        queue = collections.deque([start])
        seen = set([start])
        
        while queue:
            # Get the current node.
            node = queue.popleft()
            
            # Check if we have reached the target node.
            if node == end:
                return True
            
            # Add all neighbors to the queue.
            for neighbor in adjacency_list[node]:
                # Check if neighbor has been added to the queue before.
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        
        # Our queue is empty and we did not reach the end node.
        return False

    # DFS solution
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjacency_list = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)

        '''
            from collections import defaultdict
            
            adj_list = defaultdict(list)
            for v1, v2 in edges:
                adj_list[v1].append(v2)
                adj_list[v2].append(v1)
        '''
        
        stack = [start]
        seen = set()
        
        while stack:
            # Get the current node.
            node = stack.pop()
            
            # Check if we have reached the target node.
            if node == end:
                return True
            
            # Check if we've already visited this node.
            if node in seen:
                continue
            seen.add(node)
            
            # Add all neighbors to the stack.
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)
        
        # Our stack is empty and we did not reach the end node.
        return False