# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

''' Contributor's Code '''
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)
        
    def deserialize(self, data):
        vals = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if vals[i] == "N":
                i += 1
                return None 
            
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node 
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""



    def deserialize2(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(",")
        lst.pop() # pop the empty string "" at the end
        lst.pop() # pop the last "None" at the end
        q = collections.deque(lst)
        head = None
        trav = None
        stack = []
        left = True
        while q:
            char = q.popleft()
            if char != "None":
                node = TreeNode(char)
                if trav:
                    if left:
                        trav.left = node
                    else:
                        trav.right = node
                        left = True
                elif not head:
                    head = node
                trav = node
                stack.append(node)
            else:
                trav = stack.pop()
                left = False
        return head

    '''
    I think the serialize method given in the solution is not O(N), 
    because in the line string += str(root.val) + ',', one needs to create a copy of string first 
    because they are immutable. Hence the worst case runtime is O(N^2). 
    With a small tweak of the original idea, one can achieve O(N) runtime, as follows:
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        res = []
        dfs(root)
        return ",".join(res)


''' The second contributor '''
class Codec:
    '''       O(n) time and O(n) space, BFS traversal
    e.g., 1
         / \
        2   5
       / \
      3   4  , level order traversal, serialize will be '1,2,5,3,4,None,None,None,None,None,None,'; deserialize 
      with queue as well, convert back. Time and Space O(n).
    '''
    def serialize(self, root):
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res
            
    def deserialize(self, data):
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root