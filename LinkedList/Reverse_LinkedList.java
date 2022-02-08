public class Reverse_LinkedList {
    private class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode reverseLinkedList(ListNode head) {

        ListNode curr = head;
        ListNode prev = null;

        while(curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;

            curr = nextTemp;
        }

        return prev;
    }
    // t: 0(N)
    // s: O(1)

    public ListNode reverseLinkedListRecursive(ListNode head) {

        if (head == null || head.next == null) {
            return null;
        }

        ListNode p = reverseLinkedListRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return p;
    }

}

/**
 * Definition for singly-linked list.
 *
 */
//
// public class ListNode {
//      int val;
//      ListNode next;
//      ListNode() {}
//      ListNode(int val) { this.val = val; }
//      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
// }

