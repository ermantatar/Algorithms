# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive InOrder Traversal
    # t: O(N)
    # s: O(N)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root):
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []
    
        
        return inorder(root)[k-1]
    
    # DFS 
    # t: O(H + K), the best case O(logN + k) and the worst case O(N + k)
    # s: O(H), the best case O(logN) and the worst case O(N)
    def kthSmallest(self, root, k):
        
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
