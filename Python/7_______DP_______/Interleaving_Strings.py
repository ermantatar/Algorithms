class Solution:

    # DFS with Caching examples (all states decision tree)
    # O(m * n)
    # O(m * n)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True 
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True 
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True 

            cache[(i, j)] = False 

            return cache[(i, j)]

        # indexes of two string, s1, s2
        return dfs(0, 0)
    
    # BFS and # DFS 
    def isInterleave(self, s1, s2, s3):
        r, c, l= len(s1), len(s2), len(s3)
        
        if r+c != l:
            return False

        queue, visited = collections.deque([(0, 0), ]), set((0, 0))
        while queue:
            x, y = queue.popleft()
            if x+y == l:
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                queue.append((x+1, y)); 
                visited.add((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                queue.append((x, y+1))
                visited.add((x, y+1))
        return False

    # DP Matrix Way
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 
        
        dp = [[False] * (len(s2) + 1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True 

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True 
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True 
        
        return dp[0][0]

"""
        
   [d][b][b][c][a][]
[a][T][F][F][F][F][F]
[a][ ][ ][ ][ ][ ][]
[b][ ][ ][ ][ ][ ][]
[c][ ][ ][ ][ ][ ][]
[c][ ][ ][ ][ ][ ][] 
[ ][ ][ ][ ][ ][][t]

"""
                
    