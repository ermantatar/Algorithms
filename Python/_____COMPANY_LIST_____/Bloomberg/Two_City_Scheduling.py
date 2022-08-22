class Solution:
    """
    Algo: The main solution is to compare the choice of cost according the costB in [costA, costB] array with turning all of them [costB-costA, costA, costB]
    After this step, we need to pick the lowest cost, meaning, after sort, we need to pick first x item out of 2x total choice. 
    """
    # t: O(NlogN) s:O(N)
    def twoCityScheduleCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        diffs.sort() # will sort[0, ] using first item 
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                res += diffs[i][2] # first %50 will be from B cities
            else:
                res += diffs[i][1] # second half, pick the A cities cost. 
        
        return res




# [10, 100], [10, 1000], [10. 45000], [10, 5000000000], the goal is to pick lowest B's first.
# B city cost choices [10, 100], [10, 1000]
# A city cost choices [10. 45000], [10, 5000000000]
        