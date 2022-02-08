class Merge_K_Sorted_Lists {
    public ListNode mergeKLists(ListNode[] lists) {
        
        Comparator<ListNode> cmp = new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        };
        
        Queue<ListNode> queue = new PriorityQueue<ListNode>(cmp);
        
        for(ListNode list : lists) {
            if (list != null) {
                queue.add(list);
            }
        }
        
        ListNode head = new ListNode(0);
        ListNode curr = head;
        while(!queue.isEmpty()) {
            curr.next = queue.poll();
            curr = curr.next;
            ListNode listNext = curr.next;
            if(listNext != null) {
                queue.add(listNext);
            }
        }
        
        return head.next;
    } 
    // t: O(N * logK) where k is the number of lists. 
    // s: O(n) creating the new linkedlist costs N space, but here we do in-place algorithm. So, it is O(k) where building the priority queue take l lists. 

    public ListNode mergeKLists_divide_and_conquer(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        
        int interval = 1;
        while(interval < lists.length) {
            System.out.println(lists.length);
            for(int i = 0; i + interval < lists.length; i = i + interval*2) {
                lists[i] = mergeTwoLists(lists[i], lists[i+interval]);
            }
            interval*= 2;
        } // divide and conquer, lists are shrinking and eventually there will be one at index 0.
        
        return lists[0];
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        
        ListNode prehead = new ListNode(-1);
        
        ListNode prev = prehead;
        
        while(l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                prev.next = l1;
                l1 = l1.next;
            } else {
                prev.next = l2;
                l2 = l2.next;
            }
            
            prev = prev.next;
        }
        
        prev.next = l1 == null ? l2: l1;
        
        return prehead.next;
    }

    // t: O(N * logk)
    // s: O(1)
}


