/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

// t: O(N) // Since we processes every single node exactly once. 
// s: O(N) // This is a perfect binary tree which means the last level contains N/2 nodes.

class BFS_Solution {
    public Node connect(Node root) {
        if (root == null) return root;

        Queue<Node> Q = new LinkedList<>();
        Q.add(root);

        while(!queue.isEmpty()) {
            
            int currentQSize = Q.size();

                for(int i = 0; i < currentQsize; i++) {
                    
                    int node = Q.poll();

                    if (i < currentQSize - 1) {
                        node.next = Q.peek();
                    }

                    if (node.left != null) Q.add(node.left);

                    if (node.right != null) Q.add(node.right);
                }
        }

        return root;
    }
}

// while we are level N-1, we are connecting the next pointers of level N. This way, we got rid of queue, since we always have next pointer to move in the list.

// t: O(N)
// s: O(1)
class Next_Pointer_Solution {
    public Node connect(Node root) {

        if (root == null) return root;

        Node leftmost = root;

        while(leftmost != null) {

            Node head = leftmost;

            while(head != null) {
                // connection 1 
                head.left.next = node.right;

                if (head.next != null)  head.right.next = head.next.left;

                head = head.next;
            }

            leftmost = leftmost.left;
        }

        return root; 
    }
}