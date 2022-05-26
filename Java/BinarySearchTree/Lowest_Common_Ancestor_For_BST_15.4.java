public static BSTNode<Integer> findLCA(BSTNode<Integer> tree, BSTNode<Integer> s, BSTNode<Integer> b) {
    
    BSTNode<Integer> ptr = tree;
    
    while(ptr.data < s.data || ptr.data > b.data ) {
        // keep searching root is outside of [s, b]
        while (ptr.data < s.data) {
            ptr = ptr.right;
        }

        while (root.data > b.data) {
            ptr = ptr.left;
        }
    }

    // Now, s.data >= p.data && p.data <- b.data.
    return ptr;
}