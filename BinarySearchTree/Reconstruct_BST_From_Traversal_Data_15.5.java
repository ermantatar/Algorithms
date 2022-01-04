/*

First, with some experimentation, we see the sequence of keys 
generated by an inorder traversal is not enough to reconstruct the tree.

However, the story for a preorder sequence is different. 
As an example, con¬ sider the preorder key sequence <43,23,37, 29,31,41,47,53). 
The root must hold 43, since it's the first visited node. The left subtree contains keys 
less than 43, i.e., 23,37,29,31,41, and the right subtree contains keys greater than 
43, i.e., 47,53. Furthermore, <23,37,29,31,41> is exactly the preorder sequence for the left subtree and <47,53) 
is exactly the preorder sequence for the right subtree.


Generalizing, in any preorder traversal sequence, the first key corresponds to the root. 
The subsequence which begins at the second element and ends at the last key less than 
the root, corresponds to the preorder traversal of the root's left subtree. 
The final subsequence, consisting of keys 
greater than the root corresponds to the preorder traversal of the root's right subtree.
*/

public static BSTNode<Integer> rebuildBSTFromPreorder(List<Integer> preorderSequence) {
    return rebuildBSTFromPreorderHelper(preorderSequence, 0, preorderSequence.size())
}

// Builds a BST from preorderSequence.subList(start, end)
private static BSTNode<Integer> rebuildBSTFromPreorderHelper(List<Integer> preorderSequence, int start, int end) {
    if (start >= end) {
        return null;
    }

    // find left subtree nodes. They are smaller than the root at start.
    int transitionPoint = start + 1;
    while(transitionPoint < end && Integer.compare(preorderSequence.get(transitionPoint), preorderSequence.get(start)) < 0) {
        ++transitionPoint;
    }

    // return a root node, that has left and right subtree. 

    return new BSTNode<>(
        preorderSequence.get(start), 
        rebuildBSTFromPreorderHelper(preorderSequence, start + 1, transitionPoint), 
        rebuildBSTFromPreorderHelper(preorderSequence, transitionPoint+1, end)
    );
}



// Optimization 

class Solution {
    private static Integer rootIdx;

    public static BSTNode<Integer> rebuildBSTFromPreorder(List<Integer> preorderSequence) {
        rootIdx = 0;
        return rebuildBSTFromPreorderOnValueRange(preorderSequence, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    // Builds a BST on the subtree rooted at rootldx from preorderSequence on keys in (lowerBound, upperBound).
    private static BSTNode<Integer> rebuildBSTFromPreorderOnValueRange(List<Integer> preorderSequence, Integer lowerBound, Integer upperBound) {
        
        if (rootIdx == preorderSequence.size() {
            return null;
        }   

        Integer root = preorderSequence.get(rootIdx);
        if (root < lowerBound || root > upperBound) {
            return null;
        }

        ++rootIdx;
        // Note that rebuildBSFromPreorderOnValueRange updates rootldx. 
        // So the order of following two calls are critical.
        BSTNode<Integer> leftSubtree = rebuildBSFromPreorderOnValueRange(preorderSequence, lowerBound, root);

        BSTNode<Integer> rightSubtree = rebuildBSFromPreorderOnValueRange(preorderSequence, root, upperBound);

        return new BSTNode<>(root, leftSubtree, rightSubtree);
    }
}

//  The worst-case time complexity is 0(n), since it performs a constant amount of work per node.