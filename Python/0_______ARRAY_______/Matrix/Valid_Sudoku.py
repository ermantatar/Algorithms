class Solution:
    # Every row_i should have set, key=row_i value= collections.defaultdict(set)
    # Every col_j should have set, key=col_j value= collections.defaultdict(set)
    # Every 3x3 square should have square_set, key(row_i//3, col_j//3) value= collections.defaultdict(set)
    # The key concept here to reduce square check 9x9 to be 3x3 by looping (row_i//3, col_j//3)
    # t: O(N^2), s: O(N^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not board:
            return True 

        ROWS = len(board)
        COLS = len(board[0])
        
        col_set = collections.defaultdict(set) # k: current column, v: set
        row_set = collections.defaultdict(set) # k: current row, v: set
        square_set = collections.defaultdict(set) # k (r//3, c//3), v : set

        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == ".":
                    continue 
                
                if board[r][c] in col_set[c] or 
                    board[r][c] in row_set[r] or 
                     board[r][c] in square_set[(r//3, c//3)]:
                     return False 
                
                col_set[c].add(board[r][c])
                row_set[r].add(board[r][c])
                square_set[(r//3, c//3)].add(board[r][c])
        
        return True 

"""
[][][][][][][][][]
[][][][][][][][][]
[][][][][][][][][]
[][][][][][][][][]
[][][][][][][][][]
[][][][][][][][][]
"""