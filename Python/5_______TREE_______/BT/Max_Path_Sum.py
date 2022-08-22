class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

# https://www.youtube.com/watch?v=Hr5cWUld4vU
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

class Solution:
    # t: O(N)
    # s: O(H) h = logN

class Solution:
    # t: O(N) and s: O(H)
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-3inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node: return 0
        
        # only add positive contributions
        leftST_sum = max(0, self.dfs(node.left))
        rightST_sum = max(0, self.dfs(node.right))

        # check if cumulative sum at current node > global max sum so far
        # this evaluates a candidate path
        self.max = max(self.max, leftST_sum + rightST_sum + node.val)
        
        # add to the current node ONLY one of the children contributions
        # in order to maintain the constraint of considering only paths
        # if not, we would be exploring explore the whole tree - against problem definition
        return max(leftST_sum, rightST_sum) + node.val