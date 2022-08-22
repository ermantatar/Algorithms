from ast import List

class Solution:
    # We want to erase the intervals so that minimum amount of intervals will be conflicting. 
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # first of all, list the intervals
        intervals.sort(key=lambda x: x[0])
        
        count = 0
        prevEnd = intervals[0][1]
        
        for interval in intervals[1: ]:
            if prevEnd <= interval[0]:
                prevEnd = interval[1]
            else:
                count += 1
                prevEnd = min(prevEnd, interval[1])
        return count