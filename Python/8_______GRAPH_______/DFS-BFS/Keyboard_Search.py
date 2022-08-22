from typing import NamedTuple

'''
Given a keyboard represented as a matrix and a word, return the shortest path that would spell out the word starting from the top left corner of the matrix.

Example:
Keyboard:
A B C D E F G
H I J K L M N
O P Q R S T U
V W X Y Z * *

Word: DART

Returns:
[
    (V: 0, H: 3),
    (V: 0, H: -3),
    (V: 2, H: 3),
    (V: 0, H: 2),
]
'''


keyboard = [
    ["A", "B", "C", "D", "E", "F", "G"],
    ["H", "I", "J", "K", "L", "M", "N"],
    ["O", "P", "Q", "R", "S", "T", "U"],
    ["V", "W", "X", "Y", "Z", "", ""],
]

class Path(NamedTuple):
    V: int # vertical change... UP: V < 0; Down: V >= 0
    H: int # horizontal change... Left: H < 0; Right: H >= 0

from collections import deque 

def get_word_journey(keyboard, word):

    output = [] # Path(v,h)
    if not keyboard or not word:
        return output
    
    ROWS, COLS = len(keyboard), len(keyboard[0])
    seen = set()
    idx = 0
    origin = [0, 0]
    
    def bfs(i, j):
        nonlocal idx
        nonlocal origin

        if keyboard[i][j] == word[idx]:
            idx += 1
        
        seen.add((i, j))
        queue = deque([(i, j), ])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:

            row, col = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc 

                if new_row in range(ROWS) and new_col in range(COLS) and idx < len(word) and (new_row, new_col) not in seen:

                    if keyboard[new_row][new_col] == word[idx]:
                        # I found the character 
                        idx+= 1
                        chg_r, chg_c = new_row - origin[0], new_col - origin[1]
                        output.append(Path(chg_r, chg_c))

                        # Once I found the char, update all these 
                        while queue:
                            queue.pop()
                        origin = [new_row, new_col]
                        seen.clear()
        
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col))

    bfs(0, 0)
    return output



## Everything below this line is a test function
def test_function():
    words = {
        "DART": Path(13, 13),
        "FIG": Path(16, 9),
    }
    wrapped = False
    def get_wrapped_idx(idx, length):
        if idx < 0:
            return length + idx
        if idx > length:
            return idx % length
        return idx
    
    for word in words:
        expected_path_len = words[word]
        print(f'Testing word: {word}\n')
        journey = get_word_journey(keyboard, word)
        current = Path(0, 0)
        spelled_word = ""
        path_len = 0
        for path in journey:
            row = current.V + path.V
            col = current.H + path.H
            if wrapped:
                # get letter from wrapped
                row = get_wrapped_idx(row, len(keyboard))
                col = get_wrapped_idx(col, len(keyboard[0]))
            spelled_word += keyboard[row][col]
            current = Path(row, col)
            path_len += abs(path.V)
            path_len += abs(path.H)
        p1 = expected_path_len[0]
        if wrapped:
            p1 = expected_path_len[1]
        if spelled_word == word and path_len <= p1:
            print(f'SUCCESS: word -> {spelled_word}; length -> {path_len}\n')
        else:
            print(f'FAILED: word -> {spelled_word}; length -> {path_len}\n')
            
test_function()  
