/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */


// Floyd's Cycle Finding Algorithm
// cycle means, in the list, I will reach a item which has seen before. 

// time complexity: O(N) No cycle O(n), if cycle exist, O(N+K(inside of cycle run time)), which is O(n).
// space complexity: O(1)
class Optimal_Solution {
    public boolean hasCycle(ListNode head) {
        if (head ==null || head.next == null) { // consider the single element cases! 
            return false;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        
        do {
            slow = slow.next;
            fast = fast.next.next;
            
            // no cycle condition.
            if(fast == null || fast.next == null) {
                return false;
            }
            
        } while (slow != fast);
        
        return true;
    }
}







// time complexity: O(n)
// space complexity: O(n)
public class Solution2 {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nodeSeen = new HashSet<>();
        
        while(head!=null) {
            if (nodeSeen.contains(head)) {
                return true;
            }
            nodeSeen.add(head);
            head = head.next;
        }
        return false;
    }
}