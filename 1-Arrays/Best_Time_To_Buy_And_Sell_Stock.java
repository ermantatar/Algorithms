class Best_Time_To_Buy_And_Sell_Stock {
    public int maxProfit(int[] prices) {
        
        Integer minPrice = Integer.MAX_VALUE;
        Integer maxProfit = Integer.MIN_VALUE;
        
        for(Integer price : prices) {

            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
            
        }
        
        return maxProfit;
    }
}

// t: O(n)
// s: O(1)