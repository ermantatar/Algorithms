class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None 

class Solution:
    # t: O(N)
    # t: O(N)
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head is not None:
            if head in seen:
                return True 
            seen.add(head)
            head = head.next 
        return False 
    

    #Floyd's Cycle Algorithm 
    # t: O(N)
    # s: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False 
            
        slow = head
        fast = head.next 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
            if slow == fast:
                return True 
        
        return False
