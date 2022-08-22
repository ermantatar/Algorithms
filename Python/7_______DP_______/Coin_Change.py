class Solution:
    # t: O(amount * len(coins))
    # s: O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


"""

coin = [1, 3, 4, 5]

DP[0] = 0
DP[1] = 1
DP[2] = 2
DP[3] = 1
DP[1] = 4
DP[5] = 1
DP[6] = 2
DP[7] = 2

"""