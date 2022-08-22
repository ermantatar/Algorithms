# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # t: O(N), s:(N)
    def goodNodes_recursive(self, root: TreeNode) -> int:
        
        def dfs(node, maxValue):
            
            if not node:
                return 0
            
            maxValue = max(maxValue, node.val)
            res = 1 if node.val >= maxValue else 0
            
            res += dfs(node.left, maxValue)
            res += dfs(node.right, maxValue)
            
            return res 
        
        
        return dfs(root, root.val)
    
    def goodNodes_iterative(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        res = 0
        stack = [(root, root.val)]
        
        while stack:
            
            node, maxValue = stack.pop()
            maxValue = max(maxValue, node.val)
            
            res += 1 if node.val >= maxValue else 0
            
            if node.left:
                stack.append((node.left, maxValue))
            
            if node.right:
                stack.append((node.right, maxValue))
        
        return res 