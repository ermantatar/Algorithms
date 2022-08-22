# Second solution is correct
class Solution:
    # O(Nlogm) m is finding the correct eating speed, and N is pile iteration inside of Binary Search.
    # H: time limit, we need to finish before than that. 
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # k is the Banana eat amount, [1,....X] piles, let's find the best value in range
        l, r = 1, max(piles)
        k = 0
        
        while l <= r:
            m = (l + r) // 2
            
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / m) # (.54) all floating parts will be considered as another day. 
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k


class Solution:
    # t: O(NlogM)
    # s: O(N)

    # Optimize speed, find a number where it will keep closest smallest number to hour limit.
    # Return the first right, that satisfies this requirement. 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        l = 1
        r = max(piles)
        
        while l < r:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            m = l + (r - l) // 2            
            total_hour = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                total_hour += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if total_hour <= h:
                r = m
            else:
                l = m + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right