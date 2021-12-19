// time complexity: O(N^2), Because we are searching inside of array loop while looping inside of for.
// space complexity: O(N), Since we have declared the ArrayList. 
class Solution {
    public int singleNumber(int[] nums) {
        List<Integer> no_duplicate_list = new ArrayList<Integer>();
        
        for (int num : nums) {
            if (!no_duplicate_list.contains(num)) {
                no_duplicate_list.add(num);
            } else {
                no_duplicate_list.remove(new Integer(num));
            }
        }
        return no_duplicate_list.get(0);
    }
}

// time complexity: O(N)
// space complexity: O(N)
class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> hashTable = new HashMap<>();
        
        for (int num : nums) {
            hashTable.put(num, hashTable.getOrDefault(num, 0) + 1);
        }
        
        for (int num: nums) {
            if (hashTable.get(num) == 1) {
                return num;
            }
        }
        
        return 0;
    }
}

// time complexity: O(N)
// space complexity: O(N)
class Solution {
    public int singleNumber(int[] nums) {
        int sumOfSet = 0;
        int sumOfNums = 0;
        
        Set<Integer> set = new HashSet();
        
        for (int num : nums) {
            if (!set.contains(num)) {
                set.add(num);
                sumOfSet += num;
            }
            sumOfNums += num;
        }
        return 2 * sumOfSet - sumOfNums;
    }
}

/* ACCEPTED SOLUTION */

/*
    XOR RULE: 
    
    If we take XOR of zero and some bit, it will return that bit
        - a ⊕ 0 = a
    If we take XOR of two same bits, it will return 0
        - a ⊕ a = 0
    So; 
        - a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = b
*/

// time complexity: O(N)
// space complexity: O(1)
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        
        return result;
    }
}