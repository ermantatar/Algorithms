public static BSTNode<Integer> findFirstGreaterThanK(BSTNode<Integer> tree, Integer k) {
    BSTNode<Integer> subtree = tree, firstSoFar = null;

    while(subtree != null) {
        if (subtree.data > k) {
            firstSoFar = subtree;
            subtree = subtree.left;
        } else { // Root and All keys in left subtree are <= k, so skip them.
            subtree = subtree.right;
        }
    }

    return firstSoFar;
}

// time complexity O(H)
// space complexity O(1)