class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        
        int total_tank = 0;
        int curr_tank = 0;
        int starting_station = 0;
        for(int i = 0; i < n; i++) {
            total_tank += gas[i] - cost[i];
            curr_tank += gas[i] - cost[i];
            if (curr_tank < 0) {
                starting_station = i + 1;
                curr_tank = 0;
            }
        }
        
        return total_tank >= 0 ? starting_station : -1;
    }
}

// Time complexity : O(N) since there is only one loop over all stations here.
// Space complexity : O(1) since it's a constant space solution.

/*
Considering at each index if the gas > cost, means we are gaining some extra gas, otherwise we are losing some gas.

If the starting point exists, it must start from the position where we lose the most of the gas, 
so that it can start to gain gas first to gather all the gas we need before we start losing.
*/