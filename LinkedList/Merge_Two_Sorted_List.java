class Merge_Two_Sorted_List {
    // recursive
    public ListNode mergeTwoLists2(ListNode list1, ListNode list2) {
        
        if (list1 == null) {
            return list2;
        } else if (list2 == null) { 
            return list1;
        } else if (list1.val < list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
    // t: O(n+m)
    // s: O(n+m)
    
    // iterative
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        
        // base pointer reference for pre-head point
        ListNode prehead = new ListNode(-1);
        
        // pointer for traversing list. 
        ListNode current = prehead;
        
        while(l1 != null && l2 != null) {
            
            if(l1.val < l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            
            current = current.next;
        }
        
        current.next = l1 == null ? l2 : l1;
        
        return prehead.next;
    }
    // time complexity is: O(N + M)
    // space complexity: O(1) since we use the existent lists.
}

// t: O(N)
// s: O(1)
