# Definition for a binary tree node.
from ast import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
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

    
    # recursion
    # t: O(N)
    # s: O(N)
    def levelOrder_recursion(self, root: TreeNode) -> List[List[int]]:
        
        levels = []
        if not root:
            levels
              
        def traverse(node, level):
            # prepare for current level
            if len(levels) == level:
                levels.append([])
            
            #append the current node value
            levels[level].append(node.val)
            
            #process the child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        
        traverse(root, 0)
        return levels 
    
    
    # simplified recursion
    # t: O(N)
    # s: O(N)
    def levelOrder(self, root):
        levels = []

        def helper(node, level):
            if node:
                if len(levels) == level:
                    levels.append([])
                levels[level] += [node.val] # levels[level].append(node.val)
                helper(node.left, level+1)
                helper(node.right, level+1)

        helper(root, 0)
        return levels
    
    
    
    
    