# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0
        
        def dfs(root):
            
            nonlocal max_diameter # or we could have decleared the res as res = [0] and remove this line
            
            if not root:
                return -1
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
        
            # diameter formula, () - parent - () means = L(height) + R(height) + 1 + 1
            max_diameter = max(max_diameter, left_height + right_height + 2)
            
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return max_diameter