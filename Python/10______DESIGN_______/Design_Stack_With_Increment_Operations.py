"""
Algo:
The main idea is to not increment bottom k elements directly. Only increment top element in that bottom k elements, every time you pop, just increase the item behind the top Kth element. 
Increment bottom K element, in a lazy manner. 
"""


class CustomStack:
    # All of them O(1) operations
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.curr_size = 0
        self.data = [[0, 0] * self.max_size]
    
    def push(self, x: int) -> None:
        if self.curr_size < self.max_size:
            self.data[self.curr_size] = [val, 0]
            self.curr_size += 1
    
    def pop(self)->int:
        if self.curr_size <= 0:
            return -1 
        
        val, inc = self.data[self.curr_size-1]
        self.curr_size -= 1

        self.curr_size > 0:
            self.data[self.curr_size-1][1] += inc 
        
        return val + inc 
    
    def increment(self, k:int, val:int) -> None:
        self.data[min(self.curr_size-1, k-1)][1] += val 