# Definition for a binary tree node.
from ast import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursion 
    # t: O(N)
    # s: O(N)
    def levelOrder(self, root):
        levels = []
        
        def traverse(node, level):    
            if not node:
                return 
            
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                traverse(node.left, level + 1)
            
            if node.right:
                traverse(node.right, level + 1)
        
        traverse(root, 0)
        return levels
    """
    Algorithm
        Create levels array in the main scope, this will be result array
        Create inner function called helper and send the helper(root, 0)
        Second parameter is level 
        Check if input node is available, if so compare if len(levels) == level
        This means, it is time to introduce new level inner array []
        Then add the node value into its level inner array
        Call function with left and right childs
    """
    
    # Iteration Algorithm:
    # t: O(N)
    # s: O(N)
    def levelOrder(self, root: TreeNode)-> List[List[int]]:
        
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        
        while queue:
            #start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                #fullfill the current level
                levels[level].append(node.val)
                
                # add the child nodes of the current level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            #go to next level
            level += 1
        
        return levels
    
    """
    Iteration Algorithm:
        Decleare levels array 
        First of all check input root, if None send, empty result array
        Prepare queue with deque([root, ]) and current_level = 0
        while queue, first prepare, levels.append([]), and level_length = len(queue)
        for _ range(level_length), pop the node from queue, add the level array
        If current node.left add queue, node.right valid? add queue
        After foor loop, increase the current level 
        return levels
    """
    
    
    
        