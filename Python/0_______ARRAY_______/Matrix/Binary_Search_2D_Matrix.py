class Solution:
    # t: O(LogN), s: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # First binary search on the rows to find where target is located, which row?
        top, bottom = 0, ROWS-1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        
        # If we detect that elif case, decrease the bottom lower than top, 
        # this can happen if target is not here at all
        if top > bottom:
            return False 
        
        
        # Now we detect which row, target is located. 
        row = matrix[mid] # row where the target is located in it. 

        l, r = 0, COLS-1
        while l <= r:
            m = l + (r - l) // 2
            if target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
            else:
                return True 
        
        return False