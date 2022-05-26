class Solution:
    # Approach3: Simplification of the reversive method. 
    # t: O(N)
    # s: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        # Pass 1: Remove all invalid ")"
        first_pass_chars = []
        balance = 0
        open_seen = 0
        
        for c in s:
            if c == "(":
                balance +=1
                open_seen +=1
            if c == ")":
                if balance == 0:
                    continue
                balance -=1
            first_pass_chars.append(c)
        
        # Pass 2: Remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance
        for c in first_pass_chars:
            if c == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue 
            result.append(c)
        
        return "".join(result)
    
    
    # Approach2: Reverse the string and reverse the open and close
    # t: O(N)
    # s: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        
        def delete_invalid_closing(string, open_symbol, close_symbol):
            string_builder = []
            balance = 0
            for c in string:
                if c == open_symbol:
                    balance +=1 
                if c == close_symbol:
                    if balance == 0:
                        continue
                    balance -=1
                string_builder.append(c)
            
            return "".join(string_builder)
        
        # Note that s[::-1] gets the reverse of s
        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        
        return s[::-1]
    
    
    # Approach 1: Using Stack, Set and StringBuilder
    # t: O(N)
    # s: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        
        indexes_to_remove = set()
        stack = []
        
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        
        indexes_to_remove = indexes_to_remove.union(set(stack))
        
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        
        return "".join(string_builder)
        