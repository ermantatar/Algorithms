# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursion Approach 
    # t: O(N)
    # s: worst case O(N), best case O(1)
    def minDepth_Recursion(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        children = [root.left, root.right]
        # if we are at leaf node
        if not any(children):
            return 1 
        
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(min_depth, self.minDepth(c))
        
        return min_depth + 1
    
    # DFS
    # t: O(N)
    # s: O(N)
    def minDepth_DFS(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        stack, min_depth = [(1, root), ], float('inf')
        
        while stack:
            
            depth, root = stack.pop()
            children = [root.left, root.right]
            
            if not any(children):
                min_depth = min(min_depth, depth)
            
            for c in children:
                if c:
                    stack.append((depth +1, c))
        
        return min_depth
    

    from collections import deque
    # BFS 
    # t: O(N)
    # s: O(N)
    def minDepth_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = deque([(1, root),])
        
        while queue:
            depth, root = queue.popleft()
            children = [root.left, root.right]
            
            if not any(children):
                return depth
            for c in children:
                if c:
                    queue.append((depth + 1, c))

        