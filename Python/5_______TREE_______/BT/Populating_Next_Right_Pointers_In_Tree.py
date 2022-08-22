# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    

class Solution:

    #BFS
    # t: O(N) all nodes are visited in tree.
    # s: O(N)
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        Q = deque([root, ])
        
        while Q:
            
            # take size of this round level, how many loop necessary?
            level_length = len(Q)
            
            for i in range(level_length):
                
                # Pop a node from the front of the queue
                node = Q.popleft()
                
                # connect every node in tree to next node in the level except last node in the level
                if i < level_length - 1:
                    node.next = Q[0] # next first item after this node
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return root
    
    # BFS question, mentality follows BFS but since pointers set, no need for queue. 
    # t: O(N) all nodes are visited in tree.
    # s: O(1)
    def connect(self, root):
        curr, nxt = root, root.left if root else None 

        while curr and nxt:
            curr.left.next = curr.right 

            if curr.next:
                curr.right.next = curr.next.left 
            
            curr = curr.next 
            if not curr:
                curr = nxt 
                nxt = curr.left 
        
        return root
