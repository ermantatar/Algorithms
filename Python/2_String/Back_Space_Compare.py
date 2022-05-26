import itertools

class Solution:
    def backspace_compare(self, S: str, T: str)->bool:
        
        def build(S)->str:
            ans = []
            for c in S:
                if c != "#":
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return build(S) == build(T)
    
    # t: O(M + N)
    # s: O(M + N)

    #two-pointer-solution
    def backspaceCompare(self, S: str, T: str) -> bool:
        def nextChar(S):
            backspace = 0
            j = len(S) - 1
            while j >= 0:
                if S[j] == '#':
                    backspace += 1
                elif backspace:
                    backspace -= 1
                else:
                    yield S[j]
                j -= 1
        
        return all(x==y for x,y in itertools.zip_longest(nextChar(S), nextChar(T)))




    #stack solution
    def backspace_compare(self, S: str, T: str)->bool:
        def build_string(S: str)->str:
            stack = []
            for char in S:
                if char != "#":
                    stack.append
                else:
                    if len(stack):
                        stack.pop()
            return "".join(stack)
