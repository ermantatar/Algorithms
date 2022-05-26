/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode subtree = root, successor = null;
        
        while(subtree != null) {
            if (subtree.val > p.val) {
                successor = subtree;
                subtree = subtree.left;
            } else {
                subtree = subtree.right;
            }
        }
        
        return successor;
    }
}