"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, nextNode: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = nextNode
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr=curr.next

        curr=head
        while curr:
            copy = oldToCopy[curr]
            
            if curr.random:
                copy.random = oldToCopy[curr.random]
            
            if curr.next:
                copy.next = oldToCopy[curr.next]
            
            curr=curr.next

        return oldToCopy[head]
        