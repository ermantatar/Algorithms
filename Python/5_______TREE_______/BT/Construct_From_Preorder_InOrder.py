# Definition for a binary tree node.
"""
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""

from ast import List


"""
Algorithm
    Remember the first item in the preorder array will be the root, it is guarenteed.
    Initial root will be the preorder's first element
    Find the root index in the inorder, like inorder.index(root), this will be division index, called div
    root.left = self.buildTree(preorder[1: div+1], inorder[:div])
    root.right = self.buildTree(preorder[div+1:], inorder[div+1:])
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # t: O(N), s: O(N)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder or not inorder:
            return None 
        
        root = TreeNode(preorder[0])
        div = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: div+1], inorder[:div])
        root.right = self.buildTree(preorder[div+1:], inorder[div+1:])
        return root 

