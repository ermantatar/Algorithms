public static boolean isBinaryTree(BinaryTreeNode<Integer> tree) {
    return areKeysInRange(tree, Integer.MIN_VALUE, Integer.MAX_VALUE);
}

public static boolean areKeysInRange(BinaryTreeNode<Integer> tree, int lower, int upper) {

    if (tree = null) {
        return true;
    } else if (Integer.compare(tree.data, lower) < 0 || Integer.compare(tree.data, upper) > 0) {
        return false;
    }

    return areKeysInRange(tree.left, lower, tree.data) && areKeysInRange(tree.right, tree.data, upper);
}


// Second Approach, previously, we were going depth into left side first, 
// even though there might be violation close to root in the right side

// Here is the optimization for that with using the queue data structure. 

public static class QueueEntry {
    
    public BinaryTreeNode<Integer> treeNode; 
    public Integer lowerBound, upperBound;
    
    public QueueEntry(BinaryTreeNode<Integer> treeNode, Integer lowerBound, Integer upperBound) {
        this.treeNode = treeNode; this.lowerBound = lowerBound; this.upperBound = upperBound;
    } 
}

public static boolean isBinaryTreeBST(BinaryTreeNode<Integer> tree) {
    Queue<QueueEntry> BFSQueue = new LinkedList<>();

    BFSQueue.add(new QueueEntry(tree, Integer.MIN_VALUE, Integer.MAX_VALUE));

    QueueEntry headEntry;
    while((headEntry = BFSQueue.poll()) != null) {
        if (headEntry.treeNode != null) {
            if (headEntry.treeNode.data < headEntry.lowerBound || headEntry.treeNode.data > headEntry.upperBound) {
                return false;
            }

            BFSQueue.add(new QueueEntry(headEntry.treeNode.left, headEntry.lowerBound, headEntry.treeNode.data));
            BFSQueue.add(new QueueEntry(headEntry.treeNode.right, headEntry.treeNode.data, headEntry.upperBound));
        }
    }

    return true;
}