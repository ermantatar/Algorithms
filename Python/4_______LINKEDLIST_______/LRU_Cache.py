
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value 
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to Node
        
        # Create mechanism where L -> LRU, MRU <-R
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left 
    
    
    def remove(self, node):
        # L -> [] [x] [] [] <- R (Double LinkedList) 
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev 
    
    # insert will take place right behind the R node. 
    def insert(self, node):
        # Always insert to right most side, since it is represented as most recent used one
        # L -> [] [] [] [x] <- R
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node
        
        node.prev, node.next = prev, nxt 
    
    def get(self, key: int) -> int:
        # check to see if key is in the cache!
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 
        
    def put(self, key: int, value: int) -> None:
        # check to see if key is already in the cache or not
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # see if we exceed the capacity!
        if len(self.cache) > self.capacity:
            # remove the LRU
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]

