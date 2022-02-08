// time complexity: O(M x N) // where M and N are the number of rows and columns respectively.
// space complexity: O(M + N)
class Set_Matrix_Zereos {
    
    public void setZeroes(int[][] matrix) {
        
        int R = matrix.length;
        int C = matrix[0].length;
        
        Set<Integer> rows = new HashSet<Integer>();
        Set<Integer> cols = new HashSet<Integer>();
        
        // Essentially, we mark the rows and columns that are to be made zero
        for(int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (matrix[i][j] == 0) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        
        // Iterate over the array once again and using the rows and cols sets, update the elements.
        for( int i = 0; i < R; i++) {
            for (int j = 0; j < C; c++) {
                if (rows.contains(i) || cols.contains(j)) {
                    matrix[i][j] = 0;
                }
            }
        }
        
    }
}

// time complexity: O(M x N) // where M and N are the number of rows and columns respectively.
// space complexity: O(1)

/* First item in the row, and the first item in the column is being set to 0 as a flag to imply all items in that row or column needs to be set to zero. */
/* First row and first column is handled at the end, since they both setting matrix[0][0] as a flag. */

class Solution {
    public void setZeroes(int[][] matrix) {
        Boolean isCol = false;
        int R = matrix.length;
        int C = matrix[0].length;
        
        for(int r = 0; r < R; r++) {
            // Since first cell for both first row and first column is the same i.e. matrix[0][0]
            // We can use an additional variable for either the first row/column.
            // For this solution we are using an additional variable for the first column
            // and using matrix[0][0] for the first row.
            if (matrix[r][0] == 0) {
                isCol = true;
            }
            
            for(int c = 1; c < C; c++) {
                // If an element is zero, we set the first element of the corresponding row and column to 0
                if (matrix[r][c] == 0) {
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }
            
        // Iterate over the array once again and using the first row and first column, update the elements.
        for (int r = 1; r < R; r++) {
            for (int c = 1; c < C; c++) {
                if (matrix[r][0] == 0 || matrix[0][c] == 0) {
                    matrix[r][c] = 0;
                } 
            }
        }

        // See if the first row needs to be set to zero as well. 
        if (matrix[0][0] == 0) {
            for (int c = 0; c < C; c++) {
                matrix[0][c] = 0;
            }
        }

        // See if the first column needs to be set to zero as well. 
        if (isCol) {
            for (int r = 0; r < R; r++) {
                matrix[r][0] = 0;
            }
        }
            
    }
}