# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursive Solution
    # t: O(N), s: O(N)
    def lowestCommonAncestor_recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
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
        
        if not root:
            return root
        
        curr_root = root
        
        while curr_root:
            
            if p.val > curr_root.val and q.val > curr_root.val:
                curr_root = curr_root.right 
            elif p.val < curr_root.val and q.val < curr_root.val:
                curr_root = curr_root.left 
            else:
                return curr_root



        

        

