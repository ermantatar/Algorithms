class Solution(object):
    # t: O(rows * cols), s: O(rows * cols)
    # DFS solution 
    def floodFill(self, image, sr, sc, newColor):
        
        ROWS, COLS = len(image), len(image[0])
        color = image[sr][sc]
        
        if color == newColor: return image
        
        def dfs(r, c):
            if image[r][c] != color:
                return 
            image[r][c] = newColor
            
            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = r + dr, c + dc
                
                if new_r in range(ROWS) and new_c in range(COLS):
                    dfs(new_r, new_c)

        dfs(sr, sc)
        return image



    # Iterative DFS/BFS solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        
        if oldColor == newColor:
            return image
                
        ROWS, COLS = len(image), len(image[0])

        queue = collections.deque([(sr, sc), ])        
        while queue:
            
            # take out of queue, and process the point
            r,c = queue.popleft()
            image[r][c] = newColor
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + dr, c + dc
                
                if new_r in range(ROWS) and new_c in range(COLS) and image[new_r][new_c] == oldColor:
                    queue.append((new_r, new_c))
            
        return image

    
