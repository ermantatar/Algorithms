class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buying State: Buying or Selling 
        # If Buy -> i + 1
        # If Sell -> i + 2 (since there is +1 cooldown)

        dp = {}
        i = 0
        
        def dfs(i, buying_state):
            if i >= len(prices):
                return 0
            if (i, buying_state) in dp:
                return dp[(i, buying_state)]
            
            if buying_state:
                buy = dfs(i+1, not buying_state) - prices[i]
                cooldown = dfs(i+1, buying_state)
                dp[(i, buying_state)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying_state) + prices[i]
                cooldown = dfs(i+1, buying_state)
                dp[(i, buying_state)] = max(sell, cooldown)
            
            return dp[(i, buying_state)]

        # Start from array's 0th index and with buying state
        return dfs(i, True)