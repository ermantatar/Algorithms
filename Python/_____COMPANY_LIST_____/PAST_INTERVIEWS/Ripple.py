from collections import defaultdict


class NumberStore:
    
    def __init__(self):
        self.list = []
    
    def put(self, num):
        self.list.append(num)

    def test(self, sum):
        hash_map = {}
        for i in range(len(self.list)):
            comp = sum - self.list[i]
            if comp in hash_map:
                return True 
            
            hash_map[self.list[i]] = i

        return False 
"""
test_obj = NumberStore()
test_obj.put(1)
test_obj.put(3)
print(test_obj.test(4)) #true
print(test_obj.test(6)) #false
test_obj.put(5)
print(test_obj.test(6)) #true
test_obj.put(1)
test_obj.put(2)
print(test_obj.test(2))
"""

from collections import defaultdict

class NumberStore:
    
    def __init__(self):
        self.list = []
        self.store = defaultdict(int)
    
    # O(N) 
    def put(self, num):

        for n in self.list:
            newSum = num + n
            self.store[newSum] = True 

        self.list.append(num)
        print(self.store)

    # O(1) 
    def test(self, sum):
        if sum in self.store:
            return True 
        return False 


test_obj = NumberStore()
test_obj.put(1)
print(test_obj.test(2)) #false
test_obj.put(3)
print(test_obj.test(4)) #true
print(test_obj.test(6)) #false
test_obj.put(5)
print(test_obj.test(6)) #true
test_obj.put(1)
test_obj.put(2)
print(test_obj.test(2)) #true







"""
    {

        1: 0
        3: 1

    }
     [1, 3, 1] 2
"""


   


# store(1)
# store(3)
# test(4) -> true
# test(6) -> false
# store(5)
# test(6) -> true
# store(1)
# test(2) -> true