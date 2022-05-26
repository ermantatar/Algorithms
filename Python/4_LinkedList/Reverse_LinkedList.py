# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # t: (n), s: (1)
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        curr = head
        while curr:
            tmp = curr.next #remember next node
            curr.next = prev # REVERSE! None, first time around 
            prev = curr
            curr = tmp
        
        return prev