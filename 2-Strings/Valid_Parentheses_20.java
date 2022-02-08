
// Time Complexity: O(N)
// Space Complexity: O(N)

class Valid_Parentheses_20 {
    
    private Map<Character, Character> map;
    
    public Solution() {
        map = new HashMap<>();
        this.map.put("}", "{");
        this.map.put(")", "(");
        this.map.put("]", "[");
    }
    
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<Character>();
        for(int i =0; i < s.length(); i++) {
            
            char c = s.charAt(i);
            if (this.map.containsKey(c)) {
                char topElement = stack.isEmpty() ? '#' : stack.pop();
                if (topElement != this.map.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        
        return stack.isEmpty();     
    }
}