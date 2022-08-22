# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# ITERATIVE DFS
# Iteration  
# t: O(N) s: worst O(N) best O(logN)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        
        return res

# ITERATIVE BFS
# Iteration  
# t: O(N) s: worst O(N) best O(logN)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root, ])
        while q:
            level_length = len(q)
            for _ in range(len(level_length)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level