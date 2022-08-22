class Solution:
    """
    Given grid: 0 empty cell, 1 fresh orange, 2 rotten orange
    Return min # of minutes until no cell has a fresh orange

    BFS: rotten will contaminate neighbors first, then propagate out

    Time: O(m x n)
    Space: O(m x n)
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue and fresh > 0:
            
            level_length = len(queue)
            
            for i in range(level_length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1 
                
            
        