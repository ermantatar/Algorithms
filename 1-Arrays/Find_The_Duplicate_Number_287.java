// https://leetcode.com/problems/find-the-duplicate-number/

// Approach 7: Floyd's Tortoise and Hare (Cycle Detection)

// time complexity: O(N)
// space complexity: O(1)
class Solution {
    public int findDuplicate(int[] nums) {

        int slow = nums[0];
        int fast = nums[nums[0]];

        while(slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }

        fast = 0;
        while(fast != slow) {
            slow = nums[slow];
            fast = nums[fast];
        }

        return fast;
    }
}

/* Solutions below won't be accepted due to time and space complexity constraints */ 


// time complexity: O(NlogN)
// space complexity: O(logN) // In Java, Arrays.sort() uses Quick Sort Algorithm, and underlying implementation uses O(LogN) space.
class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1])
                return nums[i];
        }

        return -1;
    }
}

// time complexity: O(N)
// space complexity: O(N)
class Solution {
    public int findDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<Integer>();
        for (int num : nums) {
            if (seen.contains(num))
                return num;
            seen.add(num);
        }
        return -1;
    }
}