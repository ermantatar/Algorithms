from collections import deque 


# t: O(ROWS * COLS)
# s: O(ROWS * COLS)
class Solution:
    
    def wallsAndGates(self, rooms):

        if not rooms:
            return 

        GATE = 0
        EMPTY = 2**31-1
        WALL = -1
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ROWS = len(rooms)
        COLS = len(rooms[0]) 
        
        queue = deque()
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == GATE:
                    queue.append((r, c))
                    seen.add((r, c))
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in DIRECTIONS:
                new_r, new_c = r + dr, c + dc 
                
                if new_r in range(ROWS) and new_c in range(COLS) and rooms[new_r][new_c] == EMPTY and (new_r, new_c) not in seen:
                    rooms[new_r][new_c] = min(rooms[new_r][new_c], rooms[r][c] + 1)
                    queue.append((new_r, new_c))
                    seen.add((new_r, new_c))
    