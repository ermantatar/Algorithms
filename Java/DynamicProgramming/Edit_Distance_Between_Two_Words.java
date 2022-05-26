class Edit_Distance_Between_Two_Words {
    public int minDistance(String word1, String word2) {
        
        if ( word1.length() == 0 || word2.length() == 0) {
            return word1.length()+word2.length();
        }
        
        // +1 row, +1 col for the base cases.
        int[][] matrix = new int[word1.length()+1][word2.length()+1];
        
        // init boundaries
        for (int i = 0; i < word1.length()+1; i++) {
            matrix[i][0] = i;
        }
        
        for (int j = 0; j < word2.length()+1; j++) {
            matrix[0][j] = j;
        }
        
        // DP compute 
        for (int i = 1; i < word1.length()+1; i++) {
            for(int j = 1; j < word2.length()+1; j++) {
                
                // insertion after ith index, means word[0...i] == word2[0...j-1] is the same currently, we need + 1 char after i. 
                int insertion = matrix[i][j-1] + 1;
                int deletion = matrix[i-1][j] + 1; // delete from the first word.
                int replacement = word1.charAt(i-1) == word2.charAt(j-1) ? matrix[i-1][j-1] : matrix[i-1][j-1]+1;
                
                matrix[i][j] = Math.min(replacement, Math.min(insertion, deletion));
                
            }
        }
        
        return matrix[word1.length()][word2.length()];
        
    }
}

// time complexity: O(mn)
// space complexity; O(mn)

// Good Video Explanation; 
// https://www.youtube.com/watch?v=WgmZ-5qAHJ8