# binary search on 4 grids
# in the worst case, there would be n^2 calls
class Solution:
    def countShips(self, sea, topRight, bottomLeft):
      # binary search edge case
      if topRight[0] < bottomLeft[0] or topRight[1] < bottomLeft[1]:
        return 0
      # no ships
      if not Sea.hasShips(topRight, bottomLeft): 
        return 0
      # smallest possible ship location
      if topRight[0] == bottomLeft[0] and topRight[1] == bottomLeft[1]: 
        return 1
      mx = topRight[0] + bottomLeft[0] // 2
      my = topRight[1] + bottomLeft[1] // 2
      return (countShips(self, sea, topRight, [mx, my]) +
              countShips(self, sea, [mx, my], bottomLeft) +
              countShips(self, sea, [mx, topRight[1]], [bottomLeft[0], my]) +
              countShips(self, sea, [topRight[0], my], [mx, bottomLeft[1]])