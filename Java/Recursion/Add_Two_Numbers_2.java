/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addListsRecursive(l1, l2, 0);
    }
    
    private ListNode addListsRecursive(ListNode node1, ListNode node2, int carry) {
        // base case: If we are done with adding both lists
        if (node1 == null && node2 == null) {
            if (carry > 0) {
                return new ListNode(carry);
            }
            return null;
        }
         
        int value1 = (node1 != null) ? node1.val : 0;
        int value2 = (node2 != null) ? node2.val : 0;
         
        int res = (value1 + value2 + carry) % 10;
        carry   = (value1 + value2 + carry) / 10;
         
        ListNode currentHead = new ListNode(res);
         
        ListNode node1Next = (node1 != null) ? node1.next : null;
        ListNode node2Next = (node2 != null) ? node2.next : null;
 
        currentHead.next = addListsRecursive(node1Next, node2Next, carry);
         
        return currentHead;
    }
}

// ITERATIVE
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int c = 0;
        
        while ( p!=null || q!= null) {
            int sum = ( p!=null ? p.val : 0) + (q != null ? q.val : 0) + c;
            c = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        
        if (c > 0) {
            curr.next = new ListNode(c);
        }
        
        return dummyHead.next;
    }
}

// Time complexity : O(max(m,n)). Assume that mm and nn represents the length of l1 and l2 respectively, 
// the algorithm above iterates at most max(m,n) times.

