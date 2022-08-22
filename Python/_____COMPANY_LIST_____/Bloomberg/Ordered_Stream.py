"""
Problem: We will have stream of inputs, (idKey, value) where 1 <= idKey <= n
Goal: Have a sorted (based on their keys) values, every insert, return chunk of result, in a way, when we connect them, there should be one key-sorted values array.
"""


class OrderedStream:
    def __init__(self, n):
        self.list = [None] * n 
        self.ptr = 0
    
    def insert(self, idKey: int, value: str) -> List[str]:
        # since idKey is in range [1, n], we can literally locate under array indexes. 
        self.list[idKey-1] = value 

        ans = []
        while self.ptr < len(self.list) and self.list[self.ptr] != None:
            ans.append(self.list[self.ptr])
        return ans 


"""
ptr = 0
list_len = 2
         p
["aaaaa"]["bbbbbb"]["ccccc"][][]

"""