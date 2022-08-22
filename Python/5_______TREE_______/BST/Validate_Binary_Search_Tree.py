# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive
    # t: O(N), s: O(N)
    def isValidBST(self, root: TreeNode) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False 
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))

    # Iterative:
    # Same Big O! 
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        
        while stack:
            node, lower, upper = stack.pop()
            
            if not node:
                continue
            
            if not (lower < node.val < upper):
                return False
            
            stack.append((node.left, lower, node_val))
            stack.append((node.right, node_val, upper))
        
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkIfValid(root, -2**31, 2**31-1)
    
    def checkIfValid(self, root, minRange, maxRange):
        if not root:
            return True
        if minRange >= root.val or maxRange <= root.val:
            return False
        return self.checkIfValid(root.left, minRange, root.val) and self.checkIfValid(root.right, root.val, maxRange)
