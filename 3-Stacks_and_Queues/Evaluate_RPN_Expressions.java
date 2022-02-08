class Solution {
    public static int evaluateRPN(String rpnExpression) {
        Deque<Integer> stack = new LinkedList<>();
        String delimeter = ",";
        String[] symbols = rpnExpression.split(delimeter);

        for (String token: symbols) {
            if(token.length() == 1 && "+-*/".contains(token)) {
                final int firstOperand = stack.removeFirst();
                final int secondOperand = stack.removeFirst();

                switch(token.charAt(0)) {
                    case "+":
                        stack.addFirst(firstOperand + secondOperand);
                        break;
                    case "-":
                        stack.addFirst(firstOperand - secondOperand);
                        break;
                    case "*":
                        stack.addFirst(firstOperand * secondOperand);
                        break;
                    case "/":
                        stack.addFirst(firstOperand / secondOperand);
                        break;
                    default:
                        throw new IllegalArgumentException("Malformed RPN at: " + token);
                }
            } else {
                // token is a number. 
                stack.push(Integer.parseInt(token));
            }
        }
    }
}