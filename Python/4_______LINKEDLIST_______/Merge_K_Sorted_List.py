from Queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # t: O(Nlogk) k here is the number of linkedlist, O(logk) for every insertion and removal, s: O(N)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        curr = head = ListNode(0)
        queue = []
        count = 0
        
        for l in lists:
            if l:
                count += 1
                heapq.heappush(queue, (l.val, count, l))
        
        while queue:
            _, _, curr.next = heapq.heappop(queue)
            curr = curr.next 
            
            if curr.next:
                count += 1
                heapq.heappush(queue, (curr.next.val, count, curr.next))
        
        return head.next

        
    # brute-force
    # t: O(NlogN), s: O(N)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nodes = []
        
        head = tail = ListNode(0)
        
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next 
        
        
        for v in sorted(nodes):
            tail.next = ListNode(v)
            tail = tail.next 
        
        return head.next
    
    # compare one-by-one
    # t: O(NlogK), s: O(K), heap keeps k nodes. 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        setattr(ListNode, "__lt__", lambda o1, o2: o1.val < o2.val)
        
        pq = []
        
        dummy = curr = tail = ListNode(0)
        
        for l in lists:
            if l:
                heapq.heappush(pq, l)
        
        heapq.heapify(pq)
        
        while pq:
            node = heapq.heappop(pq)
            curr.next = ListNode(node.val)
            curr = curr.next 
            node = node.next 
            if node:
                heapq.heappush(pq, node)
        
        return dummy.next 


# There is also another solution to this problem
# https://leetcode.com/problems/merge-k-sorted-lists/solution/