class Non_Overlapping_Intervals {
    public int eraseOverlapIntervals(int[][] intervals) {
        
        if (intervals.length == 0) {
            return 0;
        }
        
        Arrays.sort(intervals, (o1, o2) -> Integer.compare(o1[1], o2[1]));
        
        int prevEnd = intervals[0][1];
        int count = 0;
        for(int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < prevEnd) {
                count++;
            } else {
                prevEnd = intervals[i][1];
            }
        }
        
        return count;
    }
}