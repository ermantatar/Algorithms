/*
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
*/

/*
start=2
finish=4
[1][2][3][4][5]

Remember this; 

1)  Create a dummyHead, and dummyHead.next = head
2)  Create a pointer node for Left to Sublist (leftSublist), this should point previos of entrance of sublist 
3)  Create a pointer to traverse the sublist (curr)
4)  Protect the curr->next keeping into a temp
5)  Create a links visually in your mind,
    while(start++ < finish)
        ListNode temp = curr.next;
        curr.next -> temp.next;
        leftSub.next -> temp.next;
        leftSub.next -> temp;
        start++;

*/
// time complexity is dominated by the search for the finish(th) node, i.e.,0(f).
// space complexity is O(1)
class Solution {
    public ListNode reverseBetween(ListNode L, int start, int finish) {
        if (start == finish) {
            return L;
        }

        ListNode dummyHead = new ListNode(0, L);
        ListNode leftSub = dummyHead;
        
        int k = 1;
        while (k++ < start) {
            leftSub = leftSub.next;
        }

        // reverse the sublist
        ListNode curr = leftSub.next;
        while(start++ < finish) {
            ListNode temp = curr.next;
            curr.next = temp.next;
            temp.next = leftSub.next;
            leftSub.next = temp;
        }
        
        return dummyHead.next;
    }
}