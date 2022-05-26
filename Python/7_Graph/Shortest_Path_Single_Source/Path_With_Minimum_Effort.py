class Solution:
    '''
    Time: O(ElogV) = O(M*N log M*N), where M <= 100 is the number of rows and N <= 100 is the number of       columns in the matrix.
    Space: O(M*N)

    '''
    def minimumEffortPath2(self, heights):
        row_size, col_size = len(heights), len(heights[0])
        dist = [[math.inf] * col_size for _ in range(row_size)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] # distance, row, col
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]: continue  # this is an outdated version -> skip it
            if r == row_size - 1 and c == col_size - 1:
                return d  # Reach to bottom right
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row_size and 0 <= nc < col_size:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))
    
    '''
    Time: O(M * N * log(MAX_HEIGHT)), where MAX_HEIGHT = 10^6, M <= 100 is the number of rows and N <= 100 is the number of columns in the matrix.
Space: O(M * N)
    '''
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c, visited, threadshold):
            if r == m-1 and c == n-1: return True # Reach destination
            visited[r][c] = True
            for i in range(4):
                nr, nc = r+DIR[i], c+DIR[i+1]
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc]: continue
                if abs(heights[nr][nc]-heights[r][c]) <= threadshold and dfs(nr, nc, visited, threadshold): 
                    return True
            return False
        
        def canReachDestination(threadshold):
            visited = [[False] * n for _ in range(m)]
            return dfs(0, 0, visited, threadshold)
        
        left = 0
        ans = right = 10**6
        while left <= right:
            mid = left + (right-left) // 2
            if canReachDestination(mid):
                right = mid - 1 # Try to find better result on the left side
                ans = mid
            else:
                left = mid + 1
        return ans
                        
