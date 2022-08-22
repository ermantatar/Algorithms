
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # Approach 1: BFS, Create level array for each level of the N-Array
    # t: O(N)
    # s: O(N)
    def levelOrder1(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                # add node's children
                queue.extend(node.children)
            result.append(level)
        
        return result
        
    # Approach 2: make a new list on each iteration instead of using a single queue
    # t: O(N)
    # s: O(N)
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        previous_layer = [root]
        
        while previous_layer:
            current_layer = []
            result.append([])
            for node in previous_layer:
                result[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        
        return result 

    
    # Approach 3: Recursion
    class Solution:
    def levelOrder(self, root: Optional['Node']) -> List[List[int]]:

        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if root is not None:
            traverse_node(root, 0)
        return result