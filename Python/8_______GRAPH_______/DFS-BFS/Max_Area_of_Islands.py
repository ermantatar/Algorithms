class Solution:
    # DFS
    # t: O(m * n)
    # s: O(m * n)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):

            if r not in range(ROWS) or c not in range(COLS) or (r, c) in seen or (r, c) != "1":
                return 0
            
            seen.add((r, c))

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        
        return area

        
    # t: O(m * n) 
    # s: O(m * n)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        area = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c):
            # process the current node
            seen.add((r, c))
            queue = collections.deque([(r, c), ])
            area_count = 1
            
            while queue:
                (r, c) = queue.popleft()
                
                # explore neighbors 
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    
                    if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == 1 and (new_row, new_col) not in seen:
                            area_count += 1
                            seen.add((new_row, new_col))
                            queue.append((new_row, new_col))
            
            return area_count
        
        # Loop over the matrix, start bfs from 1's but only start from not seen ones. 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = max(area, bfs(r, c))
        
        return area


     