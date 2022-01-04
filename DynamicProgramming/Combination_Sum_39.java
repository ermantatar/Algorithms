class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        LinkedList<Integer> comb = new LinkedList<Integer>();
        
        this.backtrack(candidates, target, comb, 0, results);
        return results;
    }
    
    protected void backtrack(int[] candidates, int remainTarget, LinkedList<Integer> comb, int start, List<List<Integer>> results) {
        
        if (remainTarget < 0) {
            // exceed the scope, stop exploration.
            return;
        } else if (remainTarget == 0) {
            // make a deep copy of the current combination, since it is reference of list.
            results.add(new ArrayList<Integer>(comb));
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            // add the number into the combination
            comb.add(candidates[i]);
            this.backtrack(candidates, remainTarget - candidates[i], comb, i, results);
            // backtrack, remove the number from the combination
            comb.removeLast();
        }
    } 
}

// time complexity: O(N ^ target)
// space complexity: O(N)

// https://www.youtube.com/watch?v=yFfv03AE_vA&t=3s

// #backtracking #dp 