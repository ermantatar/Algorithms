class Solution:
    
    # BFS / DFS solution
    # t: O(M * N)
    # s: O(M * N)
    """ Turning this solution into DFS is just like one change, line 71, do pop() instead, that is it!!!"""
    def numIslands(self, grid):
        
        def bfs(r, c):
            # process the current node
            queue = collections.deque([(r, c), ])
            seen.add((r, c))
            
            while queue:
                (r, c) = queue.popleft()
                
                # explore neighbors 
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    
                    if new_row in range(ROWS) and new_col in range(COLS) 
                        grid[new_row][new_col] == "1" and (new_row, new_col) not in seen:
                            seen.add((new_row, new_col)):
                            queue.append((new_row, new_col))
                            
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        islands = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands+=1
        
        return islands

    """ DFS """
    # DFS
    # t: O(M * N)
    # s: O(M * N)
    def numIsland(self, grid):
        
        if not grid:
            return 0
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid, row, col)
        
        return count 
    
    def dfs(self, grid, row col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return 
        
        grid[i][j] = '#'

        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row, new_col = row + x, col + x
            self.dfs(grid, new_row, new_col)
    

    # BFS solution
    # t: O(M * N)
    # s: O(M * N)
    def numIslands(self, grid):
        if not grid:
            return 0 
        
        
        # Graph traversal BFS is not a recursive algorithm, it is iterative and uses a queue
        def bfs(row, col):
            visited.add((row, col))
            queue = collections.deque([(row, col), ])
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while queue:
                r, c = queue.popleft()
            
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    
                    # make sure this is a land, "1" and it is not visited, so it is brand new location
                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
        
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands
    