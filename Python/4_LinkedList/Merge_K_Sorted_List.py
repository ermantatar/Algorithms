from Queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # brute-force
    # t: O(NlogN), s: O(N)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        self.nodes = []
        head = points = ListNode(0)
        
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next 
        
        for x in sorted(self.nodes):
            points.next = ListNode(x)
            points = points.next 
        
        return head.next
    
    # compare one-by-one
    # t: O(NlogK), s: O(K), heap keeps k nodes. 
    def mergeKLists(self, lists):
        
        head = point = ListNode(0)
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
        
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next 
            node = node.next 
            if node:
                q.put((node.val, node))
        return head.next


# There is also another solution to this problem
# https://leetcode.com/problems/merge-k-sorted-lists/solution/