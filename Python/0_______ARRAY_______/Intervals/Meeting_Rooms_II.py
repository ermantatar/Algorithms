


class Solutions:

'''
	Keep meeting in the PriorityQueue (min heap) key is their end time, 
	Look the root, smallest end time and compare with new comers, if intersect, then push into min heap
	If not intersect, then pop the min heap, and use that pre-booked room. 
	return size of min heap at the end.
'''
# t: O(NlogN)
# s: O(N)
class Solution_PriorityQueue:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        # sort the meetings
        intervals.sort(key = lambda x: x[0])
        
        active_meetings = []
        heapq.heappush(active_meetings, intervals[0][1])
        
        for interval in intervals[1:]:
            
            if active_meetings[0] <= interval[0]:
                heapq.heappop(active_meetings)
            
            heapq.heappush(active_meetings, interval[1])
        
        # amount of active meeting left in the Pq
        return len(active_meetings)

    
    '''
	- Divide meetings' start and end time to two seperate array and sort. 
	- Compare start and end times, start < end then meeting count+=1 or count-=1
	'''
	def minMeetingRooms(self, intervals):
		start = sorted(i.start for i in intervals)
		end = sorted(i.end for i in intervals)
		
		res, count = 0, 0
		s, e = 0, 0
		while s < len(intervals):
			if start[s] < end[e]:
				count+= 1
				s += 1
			else:
				count -= 1
				e += 1
			res = max(res, count)
		return res 


# Sorting start and end dates into two seperate arrays and compare them.
# t: O(NlogN)
# s: O(N)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms