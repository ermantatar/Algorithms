class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

class Solution:
    # t: O(N)
    # s: O(H) h = logN
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]


        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #compute the max path sum with split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # original return is max path without split
            return root.val + max(leftMax, rightMax)
    
        dfs(root)
        return res[0]

