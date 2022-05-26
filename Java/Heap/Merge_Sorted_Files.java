private static class ArrayEntry {
    public Integer value;
    public Integer arrayId;

    public ArrayEntry(Integer value, Integer arrayId) {
        this.value = value;
        this.arrayId = arrayId;
    }
}

/*
    time complexity: N * O(logN)
    space complexity: O(N)
*/
class Solution {
    public static List<Integer> mergeSortedArrays(List<List<Integer>> sortedArrays) {
        
        List<Iterator<Integer>> iters = new ArrayList<>(sortedArrays.size());
        for(List<Integer> array : sortedArrays) {
            iters.add(array.iterator());
        }

        PriorityQueue<ArrayEntry> minHeap = new PriorityQueue<ArrayEntry>((int) sortedArrays.size(), new Comparator<ArrayEntry>(){
            @Override
            public int compare(ArrayEntry o1, ArrayEntry o2) {
                return Integer.compare(o1.value, o2.value);
            }
        });

        for(int i = 0; i < iters.size(); i++) {
            if(iters.get(i).hasNext()) {
                minHeap.add(new ArrayEntry(iters.get(i).next(), i));
            }
        }

        List<Integer> result = new ArrayList<>();
        while(!minHeap.isEmpty()) {
            ArrayEntry headEntry = minHeap.poll();
            result.add(headEntry.value);
            if (iters.get(headEntry.arrayId).hasNext()) {
                minHeap.add(new ArrayEntry(iters.get(headEntry.arrayId).next(), headEntry.arrayId));
            }
        }

        return results;
    }
}

// Leetcode 
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

// More detailed 
// https://leetcode.com/problems/merge-k-sorted-lists/solution/


// Approach 1
class BruteForce {
    public ListNode mergeKLists(ListNode[] lists) {
        List<Integer> l = new ArrayList<Integer>();

        for (ListNode ln : lists) {
            while (ln != null) {
                l.add(ln.val);
                ln = ln.next;
            }
        }

        Collections.sort(l);

        ListNode head = new ListNode(0);
        ListNode h = head;
        for (int i : l) {
            ListNode t = new ListNode(i);
            h.next = t;
            h = h.next;
        }
        h.next = null;
        return head.next;
    }
}

//Aproach 2
// Time complexity : O(kN) where k is the number of linked lists.
// O(N) space
class CompareWithOnebyOne {
    public ListNode mergeKLists(ListNode[] lists) {
        int min_index = 0;
        ListNode head = new ListNode(0);
        ListNode h = head;
        while (true) {
            boolean isBreak = true; 
            int min = Integer.MAX_VALUE;
            for (int i = 0; i < lists.length; i++) {
                if (lists[i] != null) { 
                    if (lists[i].val < min) {
                        min_index = i;
                        min = lists[i].val;
                    } 
                    isBreak = false;
                }

            }
            if (isBreak) {
                break;
            } 
            ListNode a = new ListNode(lists[min_index].val);
            h.next = a;
            h = h.next; 
            lists[min_index] = lists[min_index].next;
        }
        h.next = null;
        return head.next;
    }
}

//Aproach 2
// Time complexity : O(kN) where k is the number of linked lists.
// O(1) space
public ListNode mergeKLists(ListNode[] lists) {
    int min_index = 0;
    ListNode head = new ListNode(0);
    ListNode h = head;
    while (true) {
        boolean isBreak = true;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                if (lists[i].val < min) {
                    min_index = i;
                    min = lists[i].val;
                }
                isBreak = false;
            }

        }
        if (isBreak) {
            break;
        } 
        h.next = lists[min_index];
        h = h.next;
        lists[min_index] = lists[min_index].next;
    }
    h.next = null;
    return head.next;
}

// Approach 3
// Time complexity : O(N * logk) where k is the number of linked lists.
// O(n) Creating a new linked list costs O(n) space.
class PriorityQueue_Solution {
    public ListNode mergeKLists(ListNode[] lists) { 
        Comparator<ListNode> cmp = new Comparator<ListNode>() {  
            @Override
            public int compare(ListNode o1, ListNode o2) {
                // TODO Auto-generated method stub
                return Integer.compare(o1.val, o2.val);
            }
        };
 
        Queue<ListNode> q = new PriorityQueue<ListNode>(cmp);
        for(ListNode l : lists){
            if(l!=null){
                q.add(l);
            }        
        }
        ListNode head = new ListNode(0);
        ListNode point = head;
        while(!q.isEmpty()){ 
            point.next = q.poll();
            point = point.next; 
            ListNode next = point.next;
            if(next!=null){
                q.add(next);
            }
        }
        return head.next;
    }
}

// Approach 4
// Time complexity : O(kN) where k is the number of linked lists.
// Space complexity : O(1)
class MergeListsOneByOne {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode h = new ListNode(0);
        ListNode ans=h;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                h.next = l1;
                h = h.next;
                l1 = l1.next;
            } else {
                h.next = l2;
                h = h.next;
                l2 = l2.next;
            }
        }
        if(l1==null){
            h.next=l2;
        }
        if(l2==null){
            h.next=l1;
        } 
        return ans.next;
    }
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==1){
            return lists[0];
        }
        if(lists.length==0){
            return null;
        }
        ListNode head = mergeTwoLists(lists[0],lists[1]);
        for (int i = 2; i < lists.length; i++) {
            head = mergeTwoLists(head,lists[i]);
        }
        return head;
    }
}

// Approach 5
// Merge with Divide and Conquer
// time complexity : O(Nlogk) where k is the number of linked lists.
// space complexity : O(1)
class Divide_And_Conquer {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode h = new ListNode(0);
        ListNode ans=h;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                h.next = l1;
                h = h.next;
                l1 = l1.next;
            } else {
                h.next = l2;
                h = h.next;
                l2 = l2.next;
            }
        }
        if(l1==null){
            h.next=l2;
        }
        if(l2==null){
            h.next=l1;
        } 
        return ans.next;
    }
    
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0){
            return null;
        }
        int interval = 1;
        while(interval<lists.length){
            System.out.println(lists.length);
            for (int i = 0; i + interval< lists.length; i=i+interval*2) {
                lists[i]=mergeTwoLists(lists[i],lists[i+interval]);            
            }
            interval*=2;
        }

        return lists[0];
    }
}