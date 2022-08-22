class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        if val not in self.numMap:
            self.numList.append(val)
            self.numMap[val] = len(self.numList)-1
            return True 
        else:
            return False 
    # O(1)    
    def remove(self, valueToRemove: int) -> bool:

        if valueToRemove in self.numMap:
            idx = self.numMap[valueToRemove]
            lastVal = self.numList[-1] # last item in the list 
            self.numList[idx] = lastVal 
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[valueToRemove]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()