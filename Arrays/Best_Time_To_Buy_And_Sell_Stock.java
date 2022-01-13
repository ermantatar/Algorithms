// t: O(n)
// s: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        
        Integer minPrice = Integer.MAX_VALUE;
        Integer maxProfit = 0;
        
        for(Integer price : prices) {
            
            if (minPrice > price) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        
        return maxProfit;
    }
}