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
    public ListNode swapPairs(ListNode head) {
        // If the list has no node or has only one node left.
        if ((head == null) || (head.next == null)) {
            return head;
        }
        
        // Nodes to be swapped
        ListNode firstNode = head;
        ListNode secondNode = head.next;
        
        // Swapping
        firstNode.next = swapPairs(secondNode.next);
        secondNode.next = firstNode;
        
        // Now the head is the second node
        return secondNode; 
    }
}

// time complexity: O(N), where N is the size of the linked list.
// space complexity: O(N), stack space utilized for recursion


// Iterative Approach 

class Solution {
    public ListNode swapPairs(ListNode head) {
        // Dummy node acts as the prevNode for the head node
        // of the list and hence stores pointer to the head node.
        
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        
        ListNode prevNode = dummy;
        
        while ((head != null) && (head.next != null)) {
            
            // Nodes to be swapped 
            ListNode firstNode = head;
            ListNode secondNode = head.next;
            
            prevNode.next = secondNode;
            firstNode.next = secondNode.next;
            secondNode.next = firstNode;
            
            prevNode = firstNode;
            head = firstNode.next; // jump step
        }
        
        return dummy.next;
    }
}

// Time Complexity : O(N) where N is the size of the linked list.
// Space Complexity: O(1)