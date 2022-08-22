# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: 1-2-3-4-5-6-7
# Answer: 1-7-2-6-3-5-4->Null
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next 
        # see, if there is no fast.next, this will be null pointer exception in the second line!  
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        # Now, slow pointer is at the end of first part of the list. 
        # Time to reverse the second part of the list, so that we can iterate backward
        second = slow.next 
        prev = slow.next = None # we need to point Null at the end of the first list
        while second:
            tmp = second.next 
            second.next = prev 
            prev = second 
            second = tmp
        
        # Now, 1-2-3-4-> <-5<-6<-7
        # Merge the list
        # second is None, and prev is 7 right now
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2