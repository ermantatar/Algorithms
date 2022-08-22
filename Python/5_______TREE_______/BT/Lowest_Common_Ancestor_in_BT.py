# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        
        lca_node = None 
        
        def recurse_tree(current_node):

            nonlocal lca_node

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # If the current node is one of p or q
            curr_flag = current_node == p or current_node == q

            # Left Recursion
            left_flag = recurse_tree(current_node.left)

            # Right Recursion
            right_flag = recurse_tree(current_node.right)

            # If any two of the three flags left, right or mid become True.
            if curr_flag + left_flag + right_flag >= 2:
                lca_node = current_node

            # Return True if either of the three bool values is True.
            return curr_flag or left_flag or right_flag

        # Traverse the tree
        recurse_tree(root)
        return lca_node


"""
Algorithm:
    The main idea is to find a root node which has 2 boolean value coming up from either its childs or including itself. 

"""