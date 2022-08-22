# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    # t: O(N)
    # s: O(N) worst care tree is like a line, best O(Height) == O(logN) height of the tree, (amount of recursion stack)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False 
        # reduce the target value from that current node
        targetSum -= root.val 
        # check and see if this root is a leaf, if so, check targetSum == 0
        if not root.left and not root.right:
            return sum == 0
        else:
            # If not yet, continue down to see right or left child path. 
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
    # t: O(N)
    # s: O(N)
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, targetSum - root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
        return False 
    