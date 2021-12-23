/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 /*
time complexity: O(N): 
where N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

space complexity: O(N):
This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed binary tree could be N.
*/

class Recursive_Solution {
    
    private TreeNode ans;
    
    public Solution() {
        // Variable to store LCA node.
        this.ans = null;
    }
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        this.recurseTree(root, p, q);
        return this.ans;
    }
    
    private boolean recurseTree(TreeNode currentNode, TreeNode p, TreeNode q) {
        // If reached the end of a branch, return false.
        if (currentNode == null) {
            return false;
        }
        
        // Left Recursion. If left recursion returns true, set left = 1 else 0
        int left = this.recurseTree(currentNode.left, p, q) ? 1 : 0;
        
        // Right recursion
        int right = this.recurseTree(currentNode.right, p, q) ? 1 : 0;
        
        // if the current node equals either p or q.
        int mid = (currentNode == p || currentNode == q) ? 1 : 0;
        
        if ((mid + left + right) >= 2) {
            this.ans = currentNode;
        }
        
        // return true, if any of those flags are true, or return false;
        return (mid + left + right) > 0;
    }
}

/*
Time Complexity : O(N), where N is the number of nodes in the binary tree. 
In the worst case we might be visiting all the nodes of the binary tree.

Space Complexity : O(N). In the worst case space utilized by the stack, the parent pointer dictionary and the ancestor set, 
would be N each, since the height of a skewed binary tree could be N.
*/
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Stack for the tree traversal
        Deque<TreeNode> stack = new ArrayDeque<>();
        
        // HashMap for the parent pointers
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        
        parent.put(root, null);
        stack.push(root);
        
        // iterate until we find both the nodes p and q
        while (!parent.containsKey(p) || !parent.containsKey(q)) {
            
            TreeNode node = stack.pop();
            
            //while traversing the tree, keep saving the parent pointers
            if (node.left != null) {
                parent.put(node.left, node);
                stack.push(node.left);
            }
            
            if (node.right != null) {
                parent.put(node.right, node);
                stack(node.right);
            }
        }
        
        // Ancestors set() for the node p.
        Set<TreeNode> ancestors = new HashSet<>();
        
        // Process all ancestors for node p using parent pointers.
        while(p!=null) {
            ancestors.add(p);
            p = parent.get(p);
        }
        
        // The first ancestor of q which appears in p's ancestor set() is their lowest common ancestor.
        while(!ancestor.contains(q)) {
            q = parent.get(q);
        }
        
        // their LCA.
        return q;
    }
}

class Recursive_Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null || root==p || root==q) return root;
        TreeNode left=lowestCommonAncestor(root.left,p,q);
        TreeNode right=lowestCommonAncestor(root.right,p,q);
        return (left!=null && right!=null)?root:(left!=null)?left:right;
    }
}


// One comment
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/1636280/Java-A-summary-on-Binary-Lifting-to-find-LCA