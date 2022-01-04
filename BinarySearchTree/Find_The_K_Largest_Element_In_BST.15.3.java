public static List<Integer> findKLargestInBST(BSTNode<Integer> tree, int k) {
    List<Integer> kLargestElements = new ArrayList<>();
    findKLargestInBSTHelper(tree, k, kLargestElements);
    return kLargestElements;
}

private static void findKLargestInBSTHelper(BSTNode<Integer> tree, int k, List<Integer> kLargestElements) {
    // Perform reverse inorder traversal. 
    if (tree != null && kLargestElements.size() < k) {
        findKLargestInBSTHelper(tree.right, k, kLargestElements);
        if (kLargestElements < k) {
            kLargestElements.add(tree.data);
            findKLargestInBSTHelper(tree.left, k, kLargestElements);
        }
    }
}

// The time complexity is 0(h + k), 
// which can be much better than performing a con¬ ventional inorder walk, 
//  e.g., when the tree is balanced and k is small.

