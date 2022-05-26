/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 
public class Solution_3 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        while (headA != null) {
            ListNode pB = headB;
            while(pB != null) {
                if (headA == pB) return headA;
                pB = pB.next;
            }
            
            headA = headA.next;
        }
        return null;
    }
}

public class Solution_2 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> nodesInB = new HashSet<ListNode>();
        
        while(headB != null) {
            nodesInB.add(headB);
            headB = headB.next;
        }
        
        while(headA != null) {
            if(nodesInB.contains(headA)) {
                return headA;
            }
            headA = headA.next;
        }
        
        return null;
    }
}

// time complexity: O(N)
// space complexity: O(1)
public class Solution_3 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // measure the length of two lists. 
        int firstLength = length(headA), secondLength = length(headB);
        
        // Advances the longer list to get equal length lists. 
        if (firstLength > secondLength) {
            headA = advanceListByK(firstLength - secondLength, headA); 
        }else{
            headB = advanceListByK(secondLength - firstLength, headB);
        }
        
        while (headA != null &<& headB != null &<& headA != headB) { 
            headA = headA.next;
            headB = headB.next;
        }
        
        return headA; // nullptr implies there is no overlap between LI and L2.
        
    }
    
    private static ListNode advanceListByK(int k, ListNode L) {
        while(k-- > 0) {
            L = L.next;
        }
        return L; 
    }
    
    private static int length(ListNode L) {
        int len = 0;
        while(L!=null) {
            ++len;
            L = L.next;
        }
        return len;
    }
}


// time complexity: O(N)
// space complexity: O(1)

// Very simple math, if you make them walk the same distance, they will intersect at the same node. 
// A (first list exclusive part, amount of step count)
// B (second list exclusive part, amount of step count)
// C is the after they intersect, amount of step to finish the list. 

// First ptr walks A + C + B   
// Second ptr walks B + C + A

// then they will end up in the intersection node.
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA = headA;
        ListNode pB = headB;
        
        while (pA != pB) {
            pA = pA == null ? headB : pA.next;
            pB = pB == null ? headA : pB.next;
        }
        
        return pA;
    }
}