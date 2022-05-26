# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursive Solution
    # t: O(N), s: O(N)
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return root
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
    
    # Iterative Solution
    # t: O(N), s: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_val = p.val 
        q_val = q.val
        node = root

        while node:
            parent_val = node.val 
            
            if p_val > parent_val and q_val > parent_val:
                node = node.right 
            elif p_val < parent_val and q_val < parent_val:
                node = node.left 
            else:
                return node