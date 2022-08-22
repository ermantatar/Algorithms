# Time Complexity: O(m * n) since we have to iterate through the whole board a couple times
# Space Complexity: O(1)

class Solution:
    def candyCrush(self, board):

        # Error Checking 
        if not board:
            return board 

        done = True 
        # STEP 1: Crush Rows 
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])

                # when do we want to tag them?
                if num1 == num2 and num2 == num3 and num1 != 0:
                    # tag them all negative 
                    board[r][c] = -num1
                    board[r][c+1] = -num2 
                    board[r][c +2] = -num3 
                    done = False 


        # STEP 2: Crush Cols
        for c in range(COLS):
            for r in range(ROWS-2):
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])

                # when do we want to tag them?
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r+1][c] = -num2 
                    board[r+2][c] = -num3 
                    done = False

        # STEP 3: Gravity
        if not done:
            for c in range(COLS):
                idx = ROWS - 1
                for r in range(ROWS-1, -1, -1):
                    if board[r][c] > 0:
                        board[idx][c] = board[r][c]
                        idx -= 1

                for r in range(idx, -1, -1):
                    board[r][c] = 0 
        
        
        
        return board if done else self.candyCrush(board)
