class Solution:
    # t: O(len(coins) * amount)
    # s: O(amount)
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
        
        return dp[amount]
    
"""
The goal is to find distinct ways, such as, 
    to reach 4 with only coin 2, we have 1 solution [2,2]
    to reach 10 with only coins[2,5], we have 2,2,2,2,2 and 5,5 total 2 ways.  

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[0] [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0]
[2] [1, 0, 1, 0, 1, 0, 1, 0, 1, 0,  1,  0]
[5] [1, 0, 1, 0, 1, 1, 1, 1, 1, 0,  2,  0]
[10]

"""