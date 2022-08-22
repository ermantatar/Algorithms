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
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
    
        return inorder(root)[k-1]
    
    # DFS 
    # t: O(H + K), the best case O(logN + k) and the worst case O(N + k)
    # s: O(H), the best case O(logN) and the worst case O(N)

    """
    Algorithm:
        Decleare a stack, and while loop True:
        While root is not none, add root to stack, and assign new root to be root.left 
        When root is Null (leftist point), then pop from the stack new root, and reduce k -= 1
        If k == 0, then we found the desired node, then return node.val.. 
        If not, then assign root to be root = root.right
    """
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

