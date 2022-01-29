class Valid_Palindrome_125 {
    
    public boolean isPalindrome2(String s) {
        
        StringBuilder builder = new StringBuilder();
        
        for(char ch : s.toCharArray()) {
            if (Character.isLetterOrDigit(ch)) {
                builder.append(Character.toLowerCase(ch));
            }
        }
        
        String filteredString = builder.toString();
        String reversedString = builder.reverse().toString();
        
        return filteredString.equals(reversedString);
    }

    public boolean isPalindrome(String s) {

        for(int i = 0, j = s.length()-1; i < j; i++, j++) {
            
            while(i < j && !Character.isLetterOrDigit(s.charAt(i))) {
                i++;
            }

            while(i < j && !Character.isLetterOrDigit(s.charAt(j))) {
                j--;
            }

            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }
        }

        return true;
    }

    public boolean isPalindromeUsingStreams(String s) {
        StringBuilder builder = new StringBuilder();
        
        s.chars()
            .filter(c -> Character.isLetterOrDigit(c))
            .mapToObj(c -> Character.toLowerCase((char) c))
            .foreach(builder::append);
        
        return builder.toString().equals(builder.reverse().toString());
    }
}