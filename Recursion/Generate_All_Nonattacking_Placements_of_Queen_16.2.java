public static List<List<Integer>> nQueens(int n) {
    List<List<Integer>> result = new ArrayList<>();
    solveNQueens(n, 0, new ArrayList<>(), result);
    return result;
}

private static void solveNQueens(int n, int row, List<Integer> colPlacement, List<List<Integer>> result) {
    if (row == n) {
        // All queens are legally placed.
        result.add( new ArrayList<>(colPlacement) );
    } else { 
        for (int col = 0; col < n; ++col){
            colPlacement.add(col);
            if (isValid(colPlacement)) { 
                solveNQueens(n, row + 1, colPlacement, result);
            }
            colPlacement.remove(colPlacement.size() - 1);
        }
    }
}

// Test if a newly placed queen will conflict any earlier queens placed before.
private static boolean isValid(List<Integer> colPlacement) {
    int rowID = colPlacement.size() - 1;
    for (int i = 0; i < rowID; ++i) {
        int diff = Math.abs(colPlacement.get(i) - colPlacement.get(rowID));
        if(diff == 0 || diff == rowID - i) {
            return false;
        }
    }
    return true;
}

/*
The time complexity is lower bounded by the number of nonattacking placements. 
No exact form is known for this quantity as a function of n, but it is conjectured to tend to n!/c", 
where c * 2.54, which is super-exponential.
*/