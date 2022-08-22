class Solution:
    # BFS 
    # t: O(M * N)
    # s: O(N * N)
    def pacificAtlantic_BFS(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # Check if input is empty 
        if not matrix or not matrix[0]:
            return []
        
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for r in range(ROWS):
            pacific_queue.append((r, 0))
            atlantic_queue.append((r, COLS-1))
        
        for c in range(COLS):
            pacific_queue.append((0, c))
            atlantic_queue.append((ROWS-1, c))
        
        def bfs(queue):
            seen = set() 
            
            while queue:

                (row, col) = queue.popleft()
                seen.add((row, col))
                
                for dr, dc in directions: # Check all 4 directions
                    new_r, new_c = row + dr, col + dc
                    # Check if the new cell is within bounds
                    
                    if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in seen and matrix[new_r][new_c] >= matrix[row][col]:
                        # If we've gotten this far, that means the new cell is reachable
                        queue.append((new_r, new_c))
            
            return seen
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
    
    # DFS-Recursive
    # t: O(M * N)
    # s: O(M * N)
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]: 
            return []
        
        # Initialize variables, including sets used to keep track of visited cells
        num_rows, num_cols = len(matrix), len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(row, col, reachable):
            
            # This cell is reachable, so mark it
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                new_row, new_col = row + x, col + y
                # Check if the new cell is within bounds
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                # Check that the new cell hasn't already been visited
                if (new_row, new_col) in reachable:
                    continue
                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if matrix[new_row][new_col] < matrix[row][col]:
                    continue
                # If we've gotten this far, that means the new cell is reachable
                dfs(new_row, new_col, reachable)
        
        # Loop through each cell adjacent to the oceans and start a DFS
        for i in range(num_rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, num_cols - 1, atlantic_reachable)
        for i in range(num_cols):
            dfs(0, i, pacific_reachable)
            dfs(num_rows - 1, i, atlantic_reachable)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
                    
                    