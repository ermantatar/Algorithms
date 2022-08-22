class Solution:
    # Algorithm:
    # We will decleare max_Area and stack to keep histogram bars in stack.
    # We will iterate i, h in array, and put values in stack however,
    # If current loop height, is lover than stack.top item's height, 
    # Whenever taller item faces smaller item, taller needs to be taken out of stack, since they can't be extended anymore
    # Then, we will calculate the max area with item in the stack and its distance to current index.
    # 
    # t: O(N), s: O(N)
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair : (index, height)
        
        for i, h in enumerate(heights):
            # where should we start calculating width
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index # if smaller value can go backward and extend, then back its index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area