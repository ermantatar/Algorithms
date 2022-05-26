/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// time complexity: O(N)
// space complexity: O(N)
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levels = new ArrayList<List<Integer>>();
        if (root == null) {
            return levels;
        }
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        int level = 0;
        
        while(!queue.isEmpty()) {
            // start with a current level
            levels.add(new ArrayList<Integer>());
            
            //number of elements in the current level
            int level_length = queue.size();
            for(int i = 0; i < level_length; i++) {
                TreeNode node = queue.remove();
                
                //fullfill the current level
                levels.get(level).add(node.val);
                
                //add child node of the current level to the queue
                if (node.left != null) queue.add(node.left);
                if (node.right != null ) queue.add(node.right);
            }
            //go to next level
            level++;
        }
        return levels;
    }
}

// Leetcode Comment, it was slightly faster than previous one. 
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levels = new LinkedList<>();
        if (root == null) return levels;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new LinkedList<>();
            
            for (int i = 0; i < size; i++) {
                TreeNode current = queue.poll();
                level.add(current.val);
                
                if (null != current.left)
                    queue.add(current.left);
                if (null != current.right)
                    queue.add(current.right);
            }
            levels.add(level);
        }
        
        return levels;
    }
}