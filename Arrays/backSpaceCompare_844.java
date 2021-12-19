class Stack_Solution {

    public boolean backspaceCompare(String s, String t) {
        return build(s).equals(build(t));
    }
    
    public String build(String s) {
        Stack<Character> stack = new Stack<>();
        
        for(char c : s.toCharArray()) {
            if (c != '#') {
                stack.push(c);
            } else if (c == '#' && !stack.isEmpty()) {
                stack.pop();
            }
        }
        
        return String.valueOf(stack);
    }
}

class TwoPointer_Solution {
    public boolean backspaceCompare(String S, String T) {
        int i = S.length()-1;
        int j = T.length()-1;
        int skipS = 0;
        int skipT = 0;

        while (i >= 0 || j >= 0) {

            while(i >= 0) {
                if (S.charAt(i) == '#') { skipS++; i--;} 
                else if (skipS > 0) { skipS--; i--;} 
                else { break; }
            }

            while (j >= 0) {
                if (T.charAt(j) == '#') { skipT++; j--;}
                else if (skipT > 0) { skipT--; j--;}
                else break;
            }

            if ( i>=0 && j >= 0 && S.charAt(i) != T.charAt(j)) {
                return false;
            }

            if ((i >= 0) != (j>= 0)) {
                return false;
            }

            i--;
            j--;
        }

        return true;
    }
}



aba#b#

aa#bcc##