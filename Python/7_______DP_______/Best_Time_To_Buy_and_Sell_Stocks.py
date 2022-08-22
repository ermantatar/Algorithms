from ast import List

class Solution:
    """
    Algorithm:
    If not prices, return 0
    Define variables, minProfit is +infinity, and maxPrice is -infinity
    Loop over the prices, and calculate today's profit, price - minPrice => today's profit
    Save the maxProfit so far, maxProfit = Max(maxProfit, today's profit)
    Save the minPrice = Min(minPrice, price)
    """
    # t: O(n)
    # s: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        minPrice, maxProfit = float('inf'), 0

        for price in prices:
            
            todayProfit = price - minPrice
            maxProfit = max(maxProfit, todayProfit)
            
            minPrice = min(minPrice, price)
        
        return maxProfit