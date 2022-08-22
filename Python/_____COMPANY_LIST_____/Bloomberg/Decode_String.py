class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                # time to build inner str [xyz], don't forget x needs to before, y and z, so subStr = stack.pop() + subStr
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()

                # now, it is time to build (digit)[] located right before the []
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # time to calculate and add back to whole thing into stack 
                stack.append(int(k) * subStr)
        
        return "".join(stack)
