class Solution:
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
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
    
        def bfs(r, c):
            if grid[r][c] == "0": 
                return 0
            Q = deque([(r, c)])
            while Q:
                r, c = Q.popleft()
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    
                    nr, nc = r + x, c + y
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == "0": 
                        continue
                    grid[nr][nc] = "0"  # Mark as visited
                    Q.append([nr, nc])
            return 1
    
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += bfs(r, c)
        return ans
    