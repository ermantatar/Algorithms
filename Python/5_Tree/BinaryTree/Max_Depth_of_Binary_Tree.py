# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # t: O(N) s: worst: O(N), best O(logN)
    def maxDepth_1(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    '''
        iteration
        # t: O(N) s: worst O(N) best O(logN)
    '''
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))
        
        max_depth = 0
        while stack != []:
            current_depth, current_node = stack.pop()
            if current_node is not None:
                max_depth = max(max_depth, current_depth)
                stack.append((current_depth + 1, current_node.left))
                stack.append((current_depth + 1, current_node.right))
        
        return max_depth