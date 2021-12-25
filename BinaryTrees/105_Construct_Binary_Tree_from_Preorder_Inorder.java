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

 /*
Time complexity : O(N):
Building the hashmap takes O(N) time, as there are N nodes to add, 
and adding items to a hashmap has a cost of O(1), so we get N*O(1) = O(N)⋅O(1)=O(N).

Building the tree also takes O(N) time. The recursive helper method has a cost
of O(1) for each call (it has no loops), and it is called once for each of 
the N nodes, giving a total of O(N).
Taking both into consideration, the time complexity is O(N).

Space Complexity O(N):

Building the hashmap and storing the entire tree each requires O(N) memory. 
The size of the implicit system stack used by recursion calls depends on the 
height of the tree, which is O(N) in the worst case and O(logN) on average. 
Taking both into consideration, the space complexity is O(N).



 */
class Solution {
    
    int preorderIndex;
    Map<Integer, Integer> inorderIndexMap;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        preorderIndex = 0;
        // build a hashmap to store value -> its index relations
        inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }

        return arrayToTree(preorder, 0, preorder.length - 1);
    }

    private TreeNode arrayToTree(int[] preorder, int left, int right) {
        // if there are no elements to construct the tree
        if (left > right) return null;

        // select the preorder_index element as the root and increment it
        int rootValue = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootValue);

        // build left and right subtree
        // excluding inorderIndexMap[rootValue] element because it's the root
        root.left = arrayToTree(preorder, left, inorderIndexMap.get(rootValue) - 1);
        root.right = arrayToTree(preorder, inorderIndexMap.get(rootValue) + 1, right);
        return root;
    }
}

class DFS_Solution {
    int index = 0;
    Map<Integer, Integer> map;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length == 0
            || preorder.length != inorder.length) return null;
        map = buildMap(inorder);
        return dfs(inorder, preorder, 0, inorder.length - 1);
    }
    
    public TreeNode dfs(int[] inorder, int[] preorder, int start, int end) {
        if (start > end) return null; // catch dfs attempting to process visisted nodes
        int rootVal = preorder[index++];
        int rootInd = map.get(rootVal);
        TreeNode root = new TreeNode(rootVal);
        if (start == end) return root;
        
        root.left = dfs(inorder, preorder, start, rootInd - 1);
        root.right = dfs(inorder, preorder, rootInd + 1, end);
        
        return root;
    }
    
    private Map<Integer, Integer> buildMap(int[] inorder) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) map.put(inorder[i], i);
        return map;
    }
}