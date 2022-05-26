


class Solutions:
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


'''
- Divide meetings' start and end time to two seperate array and sort. 
- Compare start and end times, start < end then meeting count+=1 or count-=1
'''

class Solution_PriorityQueue:
	def minMeetingRooms(self, intervals: List[List[int]])->int:
		# If there is no meeting to schedule then no room needs to be allocated.
		if len(intervals) == 0:
			return 0

		# heap initialize
		freeRooms = []

		# Sort the meetings in increasing order of their start time.
		heap