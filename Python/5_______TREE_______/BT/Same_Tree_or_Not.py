from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Algorithm:
    Recursion:
    We have been given p and q nodes, and our goal is to understand if p and q are same tree or not?
    First check, if both of them are Null, then it is True 
    Second check, if one of them are Null, or their value is not equal to each other, then it is False 
    So, far, if we reach this level, we know that their roots are equal to each other, however, this is not enough! 
    We need to recursively call our function two times, one for function(p.left, q.left) and function(p.right, q.right)

    Iteration: 
    We need to create a deque = deque([(p, q), ]), and send the p and q's root pair as a first item to deque.
    We can create nested helper function check for (not p and not q) return True, (not p or not q) return False, (p.val != q.val) return False if not hit any of them return True 
    While deque: we can pop p, q from deque, if not function_check(p, q): return False 
    If they are equal so far, then we can check if p and q: then deque.append((p.left, q.left)) and deque((p.right, q.right)) 

"""

class Solution:
    # Recursion 
    # t: O(N) s: (N) or (logN)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False 
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

    def isSameTree(self, p: 'Optional[TreeNode]', q: 'Optional[TreeNode]') -> bool:
        
        def check(p, q):
            if not p and not q:
                return True
            if (not p or not q) or p.val != q.val:
                return False 
            
            return True
        

        deq = deque([(p, q),])
        
        while deq:
            p, q = deq.popleft()
            
            if not check(p ,q):
                return False 
            if p and q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True