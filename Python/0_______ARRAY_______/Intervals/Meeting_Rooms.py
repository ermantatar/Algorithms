class BruteForce_Solution:

    # t: O(n^2)
    # s: O(1)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    	
        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            return (min(interval1[1], interval2[1]) > max(interval1[0], interval2[0]))
            # return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]) or (interval2[0] >= interval1[0] and interval2[0] < interval1[1])
        
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True





# Sorting option
class Solutions:
    # t: O(NlogN)
    # s: O(1)
	def canAttendAllMeetings(self, intervals: List[List[int]]) -> bool:
        # Sorted according to start date of meetings.
        # See if, earliest one's ending is intersection next one's starting time. 
		intervals.sort(key = lambda interval: interval[0])
		for i in range(len(intervals)-1):
			if intervals[i][1] > intervals[i+1][0]:
				return False

		return True