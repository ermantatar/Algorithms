class Solution: 
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
    
    def functionToSolveProblem(self, weatherArray: List[List[str]], root: Optional[TreeNode], k: int) -> bool: 
    




class Solution:
    def allPathsSourceTarget(self, graph):
        self.n = len(graph)
        def dfs(i):
            if i == self.n - 1: return [[self.n - 1]]
            if len(graph[i]) == 0:
                return [[]]

            res = []
            for j in graph[i]:
                for path in dfs(j):
                    if len(path) > 0:
                        res.append([i] + path)
            # print(i, path)
            return res     
        return dfs(0)

s = Solution()
graph = [[1,2], [3], [3], []] 
print(s.allPathsSourceTarget(graph))