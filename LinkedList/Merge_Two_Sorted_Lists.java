// Elements of Programming Interview Book, Chapter 8-1

// time complexity is: O(N + M)
// space complexity: O(1) since we use the existent lists.
class Solution {
    public static ListNode<Integer> mergeTwoSortedLists (ListNode<Integer> L1, ListNode<Integer> L2) {
        // placeholder for the result
        ListNode<Integer> dummyHead = new ListNode<>(0, null);
        ListNode<Integer> current = dummyHead;
        ListNode<Integer> p1 = L1, p2 = L2;

        while (p1 != null && p2 != null) {
            if (p1.data <= p2.data) {
                current.next = p1;
                p1 = p1.next;
            } else {
                current.next = p2;
                p2 = p2.next;
            }
            current = current.next;
        }

        // Appends the remaining nodes of p1 or p2. 
        current.next = p1 != null ? p1 : p2;
        return dummyHead.next;
    }
}