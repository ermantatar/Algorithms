class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # take an example [10, 15, 20] 0 , here 0 will be the final step cost
        cost.append(0)

        # we want to start from the 15 in the example above since 20 won't be changing. It can only do 1 step and reach to destination. 
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1]) 
