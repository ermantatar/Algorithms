class Node:
    def __init__(self):
        self.val = value 
        self.next = None 
        self.prev = None 
        self.child = None 

# t: O(N), s: O(N)
class Solution:
    def flatten(self, head: Node) -> Node:
        if not head: return head 

        dummy = Node(0)
        curr, stack = dummy, [head]
        while stack:
            node = stack.pop()
            if node.next: 
                stack.append(node.next)
            if node.child: 
                stack.append(node.child)
            curr.next = node 
            node.prev = curr 
            node.child = None 
            curr = node 
        # remove initial dummy connection with the list itself
        dummy.next.prev = None 
        return dummy.next