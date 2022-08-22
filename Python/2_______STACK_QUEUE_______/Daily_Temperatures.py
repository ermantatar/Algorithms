class Solution:
    # Algorithm 
    # We have array of temperature values, and our goal is to create output array 
    # Showing that how long it take to observe higher value of that index
    # [73,74,75,71,69,72,76,73]
    # [1,1,4,2,1,1,0,0]
    # So, we will use stack to keep [temp, index] pairs and pop them when we see higher value
    # While popping, we can sign their index, with the current index difference i - stack_idx
    # This will automatically create everyone's result value, if not, 0 will be assigned. 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # result array 
        stack = [] # pair [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = (i - stack_idx) # how long it take to find higher value
            stack.append([t, i])
        return res
