# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Algorithm:
    First solve the Same_Tree_Or_Not.py
    Now,
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False 
        
        if self.sameTree(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node1:
            return True
        if (not node1 or not node2) or (node1.val != node2.val):
            return False 
        
        return (self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)) 