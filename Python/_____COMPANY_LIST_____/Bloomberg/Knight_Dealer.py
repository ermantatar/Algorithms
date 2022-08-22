class Solution:
    def __init__(self):
        self.res = collections.defaultdict(int)
        self.digitMap = {'0': ['4','6'],
                          '1': ['6','8'],
                          '2': ['7','9'],
                          '3': ['4','8'],
                          '4': ['9'],
                          '5': [],
                          '6': ['1','7'],
                          '7': ['2','6'],
                          '8': ['1','3'],
                          '9': ['4','3']
                        }
    
    def recursion(self, n, digit):
      print(n, digit)
      if n in self.res:
        return self.res[(n,digit)]
      
      if n == 1:
        self.res[(n,digit)] =  min(len(self.digitMap[digit]),1)
        return self.res[(n,digit)]
      
      res = 0
      for i in self.digitMap[digit]:
        res += self.recursion(n - 1, i)
      return res

    def knightDialer(self, n):
      sol = 0
      for key in self.digitMap.keys():
        sol += self.recursion(n, key)
      return sol

    def dp():
      return

n = 10101
n = 2
sol = Solution()
print(sol.knightDialer(n))
print(sol.res)