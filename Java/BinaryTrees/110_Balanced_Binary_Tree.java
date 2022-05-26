
//https://leetcode.com/problems/balanced-binary-tree/solution/
// Top Down Approach (includes redundancy, child node's height get calculated for every parent)
// time complexity: O(NlogN) // see the explanation, in the leetcode solution.
// space complexity: O(N) // The recursion stack may contain all nodes if the tree is skewed.
class Solution_2 {
    // Recursively obtain the height of a tree. An empty tree has -1 height
    public boolean isBalanced(TreeNode root) {
        // An empty tree satisfies the definition of a balanced tree
        if (root == null) {
            return true;
        }
        
        return Math.abs(height(root.left) - height(root.right)) < 2 
            && isBalanced(root.left) && isBalanced(root.right);
    }
    
    private int height(TreeNode root) {
        // An empty tree has height -1
        if (root == null) {
            return -1;
        }
        
        return 1 + Math.max(height(root.left), height(root.right));
    }
}


// time complexity: O(N)
// space complexity: O(N) The recursion stack may go up to O(n) if the tree is unbalanced.

// new Utility Class to store information from recursive calls.
final class TreeInfo {
    public final int height;
    public final boolean balanced;
    
    public TreeInfo(int height, boolean balanced) {
        this.height = height;
        this.balanced = balanced;
    }
}

class Solution {
    
    public boolean isBalanced(TreeNode root) {
        return isBalancedTreeHelper(root).balanced;
    }
    
    // Return whether or not the tree at root is balanced while also storing
    // the tree's height in a reference variable. 
    public TreeInfo isBalancedTreeHelper(TreeNode root) {
        
        // An empty tree is balanced and has height = -1
        if (root == null) {
            return new TreeInfo(-1, true);
        }
        
        // Check subtrees to see if they are balanced.
        TreeInfo left = isBalanced(root.left);
        if (!left.balanced) {
            return new TreeInfo(-1, false);
        }
        
        TreeInfo right = isBalanced(root.right);
        if(!right.balanced) {
            return new TreeInfo(-1, false);
        }
        
        // Use the height obtained from the recursive calls to
        // determine if the current node is also balanced.
        if (Math.abs(left.height - right.height) < 2) {
            return new TreeInfo(Math.max(left.height, right.height) + 1, true);
        } else {
            return new TreeInfo(-1, false);
        }
    }
    
    
}