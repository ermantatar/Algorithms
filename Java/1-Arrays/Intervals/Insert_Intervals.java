class Insert_Intervals {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // init data
        int newStart = newInterval[0], newEnd = newInterval[1];
        int idx = 0, n = intervals.length;
        LinkedList<int[]> output = new LinkedList<int[]>();
        
        // add all intervals starting before newInterval
        while(idx < n && newStart > intervals[idx][0]) {
            output.add(intervals[idx++]);
        }
            
        // add interval
        int[] interval = new int[2];

        // if there is no overlap, just add the interval
        if (output.isEmpty() || output.getLast()[1] < newStart) {
            output.add(newInterval);
        } else { // if there is an overlap, merge with the last interval
            interval = output.removeLast();
            interval[1] = Math.max(interval[1], newEnd);
            output.add(interval);
        }
        
        // add next intervals, and merge with newIntervals if needed. 
        while(idx < n) {
            interval = intervals[idx++];
            int start = interval[0], end = interval[1];
            // if there is no overlap, just add an interval
            if (output.getLast()[1] < start) {
                output.add(interval);
            } else { // if there is an overlap, merge with the last interval
                interval = output.removeLast();
                interval[1] = Math.max(interval[1], end);
                output.add(interval);
            }
        }
        return output.toArray(new int[output.size()][2]);
    }
    
    public int[][] insert_second(int[][] intervals, int[] newInterval) {
        // init data
        int newStart = newInterval[0], newEnd = newInterval[1];
        int idx = 0, n = intervals.length;
        ArrayList<int[]> output = new ArrayList<int[]>();

        // add all intervals before newInterval
        while (idx < n && intervals[idx][1] < newStart)
          output.add(intervals[idx++]);

        // merge newInterval
        int[] interval = new int[2];
        while(idx < n && intervals[idx][0] <= newEnd)
        {
            newStart = Math.min(newStart, intervals[idx][0]);
            newEnd = Math.max(newEnd, intervals[idx][1]);
            ++idx;
        }   
        output.add(new int[]{newStart, newEnd});

        // add all intervals after newInterval  
        while (idx < n)
          output.add(intervals[idx++]);

        return output.toArray(new int[0][0]);
    }
}
// t: O(N) since it's one pass along the input array.
// s: O(N)