from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        minPrice, maxProfit = float('inf'), 0

        for price in prices:
            
            todayProfit = price - minPrice
            maxProfit = max(maxProfit, todayProfit)
            minPrice = min(minPrice, price)
        
        return maxProfit
    # t: O(n)
    # s: O(1)