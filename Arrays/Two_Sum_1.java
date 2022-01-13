// t: O(N)
// s: O(N)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        if (nums.length == 0) return new int[]{};
        
        Map<Integer, Integer> table = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++) {
            if (table.containsKey(target - nums[i])) {
                return new int[]{table.get(target - nums[i]), i};
            } 
            
            table.put(nums[i], i);
        }
        return new int[]{};
    }
}