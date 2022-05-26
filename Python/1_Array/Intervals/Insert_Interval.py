from ast import List


class Solution:
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #init data
        newStart, newEnd = newInterval
        idx, n = 0, len(intervals)
        output = []

        # add all intervals starting before newInterval
        while idx < n and intervals[idx][1] < newStart:
            output.append(intervals[idx])
            idx+=1
        
        #add interval, if there is no overlap, just add | or merge if there is intersection
        if not output or output[-1][1] < newStart:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newEnd)
        
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx +=1 
             # if there is no overlap, just add an interval
            if output[-1][1] < start:
                 output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        
        return output 
    
    # t: O(N)
    # s: O(N)





        



        
