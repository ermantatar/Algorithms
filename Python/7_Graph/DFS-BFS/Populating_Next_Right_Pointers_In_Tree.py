# Definition for a Node.
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
        
        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])
        
        # Outer while loop which iterates over 
        # each level
        while Q:
            
            # Note the size of the queue 
            size = len(Q)
            
            # Iterate over all the nodes on the current level
            for i in range(size):
                
                # Pop a node from the front of the queue
                node = Q.popleft()
                
                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0] # next first item after this node
                
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return root
    
    # BFS question, mentality follows BFS but since pointers set, no need for queue. 
    # t: O(N) all nodes are visited in tree.
    # s: O(1)
    def connect(self, root):
        curr, next = root, root.left if root else None 

        while curr and next:
            curr.left.next = curr.right 

            if curr.next:
                curr.right.next = curr.next.left 
            
            curr = curr.next 
            if not curr:
                curr = next 
                next = curr.left 
        
        return root
