from ast import List


class Solution:
    # Algorithm
    # If intervals list is empty, add right away and return it. 
    # Loop the intervals, check if newInterval[1] < list_interval[i][0]: if so, add the newInternal to res, then res + intervals[i:]
    # During the loop, if  list_interval[i][1] < newInterval[0]: res.append(list_interval[i])
    # There is intersection, then min of initials, max of ends, mix current_list_interval with new_interval, continue to iteration
    # t: O(N)
    # s: O(N)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        if not intervals:
            res.append(newInterval)
            return res 
        
        for i in range(len(intervals)):
    
            if intervals[i][1] < newInterval[0]:
                # If intervals 's item is before than new interval, add them into the result array. 
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                # If newInterval's end time is smaller than the next item in array, add newInterval and + all rest of the array. 
                res.append(newInterval)
                return res + intervals[i:]
            else:
                # If there is a intersection, earliest start date and latest end date needs to be considered. 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        
        return res
    # t: O(N)
    # s: O(N)
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
    
    





        



        
