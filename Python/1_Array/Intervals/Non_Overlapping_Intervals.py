from ast import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        count = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1: ]:
            if start < prevEnd:
                count+=1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return count