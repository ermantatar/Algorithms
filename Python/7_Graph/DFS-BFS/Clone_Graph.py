
class Solution:

    # dfs iteratively
    def cloneGraph(self, node):
        if not node:
            return node
        
        adj_matrix, visited, stack = dict(), set(), deque([node])
        
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            
            visited.add(node)
            if node not in adj_matrix:
                adj_matrix[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                if neighbor not in adj_matrix:
                    adj_matrix[neighbor] = Node(neighbor.val)
                adj_matrix[node].neighbors.append(adj_matrix[neighbor])
                stack.append(neighbor)
        
        return adj_matrix[node]

    # dfs recursively
    def cloneGraph_recursive(self, node):
        if not node:
            return node 
        
        adj_matrix, visited = dict(), set()
        self.dfs(node, adj_matrix, visited)
        return adj_matrix[node]
    
    def dfs(self, node, adj_matrix, visited):
        if node in visited:
            return 
        visited.add(node)

        if node not in adj_matrix:
            adj_matrix[node] = Node(node.val)
        
        for neighbor in node.neighbors:
            if neighbor not in adj_matrix:
                adj_matrix[neighbor] = Node(neighbor.val)
            adj_matrix[node].neighbors.append(adj_matrix[neighbor])
            self.dfs(neighbor, adj_matrix, visited)

    
    # bfs
    def cloneGraph1(self, node):
        if not node:
            return node
        m, visited, queue = {}, set(), collections.deque([node])
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                queue.append(neigh)
        return m[node]

    
    #another bfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]

