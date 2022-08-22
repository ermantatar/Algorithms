# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS 
    # t: O(N) 
    # s: O(D) diameter
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        queue = deque([root,])
        rightside = []
        
        while queue:
            # Use level length in down below when checking the last element in the queue, 
            # since queue length is changing in every pop.
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                
                # add child node in the queue
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                # add last node into rightside array 
                if i == level_length-1:
                    rightside.append(node.val)
            
        return rightside
    
    # DFS
        # t: O(N)
        # s: O(H)
        def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            
            if root is None:
                return []
            
            rightside = []
            
            def helper(node, level):
                if level == len(rightside):
                    rightside.append(node.val)
                
                for child in [node.right, node.left]:
                    if child:
                        helper(child, level + 1)
            
            helper(root, 0)
            return rightside
    
    '''
    Algorithm: Let's use two queues: one for the current level, and one for the next. The idea is to pop the nodes one by             one from the current level and push their children into the next level queue. Each time the current queue is     empty, we       have the right side element in hands.
    '''
    # BFS with two queues
    # t: O(N)
    # s: O(D) diameter of the tree, the last level can contain up to N/2 tree nodes
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        # start with creating a queue called next_level 
        # initial phase of every round, assign current_level = next_level, next_level = deque() 
        next_level = deque([root,])
        rightside = []
        
        while next_level:
            
            curr_level = next_level
            next_level = deque()
            
            while curr_level:
                node = curr_level.popleft()
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # last node will come here
            rightside.append(node.val)
        
        return rightside
        
        # BFS same approach with 1 queue, and None values as sentinel value 
        # t: O(N)
        # s: O(D) diameter of the tree    
        def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            
            if root is None:
                return []
            
            queue = deque([root, None,])
            rightside = []
            
            curr = root
            while queue:
                prev, curr = curr, queue.popleft()
                
                while curr:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    
                    prev, curr = curr, queue.popleft()
                
            # the current level is finished
            # and prev is its rightmost element
            rightside.append(prev.val)
            # add a sentinel to mark the end 
            # of the next level
            if queue:
                queue.append(None)
            
            return rightside
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                