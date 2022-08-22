# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
class Solution:
    def addTwoNumbers(self, l1, l2 , c = 0):
        
        # process the current round 
        val = l1.val + l2.val + c
        ret = ListNode(val % 10)
        c = val // 10
         
        # See, if there is one of them exist to go next digit, if so, prepare and go
        if l1.next or l2.next or c != 0:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
    # Algorithm
    # First of all, create a dummy_node, and assign with ListNode(0) and also curr the same thing
    # while l1 or l2 or c: and check if l1 is not null, then c += l1.val then l1 = l1.next
    # if l2 is there, then c += l2.val then l2 = l2.next
    # after that, curr.next = ListNode()
    def addTwoNumbers_Iterative(self, l1, l2):
        
        dummy = curr = ListNode(0)
        c = 0
        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            
            curr.next = ListNode(c % 10)
            c //= 10
            
            cur = cur.next
        
        return dummy.next