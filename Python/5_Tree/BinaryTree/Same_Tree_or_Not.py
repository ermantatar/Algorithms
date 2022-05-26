from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        
        deq = deque([(p, q),])

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False 
            if p.val != q.val:
                return False
            return True
        
        while deq:
            p, q = deq.popleft()
            
            if not check(p ,q):
                return False 
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True