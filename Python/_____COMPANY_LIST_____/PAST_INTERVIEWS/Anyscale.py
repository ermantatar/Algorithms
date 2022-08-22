from typing import Tuple

# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!

# Question:
# There are two large files containing SORTED key value pairs, where keys are strings and values are integers. e.g.

# File 1:

# aaa: 1
# bbb: 5
# bbb: 3
# ccc: 2

# File 2:

# bbb: 9
# ccc: 10
# ddd: 11

# We want to merge the two files together to produce an output file where keys are still sorted. Consecutive pairs with the same key in the output are merged, by summing up their values. e.g. merging the files above produces the output:

# aaa: 1
# bbb: 17
# ccc: 12
# ddd: 11


# API to read from the input file. Example usage:
#
#   while input_stream.is_valid():
#       key, val = input_stream.read()
#       ......
#       input_stream.next()
#
# Testing can be done by providing data via the constructor.
class InputStream:
    # For testing, InputStream can be constructed from a list.
    def __init__(self, data):
        self._data = data
        self._current = 0
    
    # Checks whether the stream has data at the current position.
    # Returns false if the stream is already ended.
    def is_valid(self):
        return self._current < len(self._data)
    
    # Gets the current pair.
    # NOTE: does not advance position in the stream.
    # Returns None if the stream has already ended.
    def read(self) -> Tuple[str, int]:
        if self.is_valid():
            return self._data[self._current]
        return None
    
    # Advances to the next item in the stream.
    def next(self):
        if self.is_valid():
            self._current += 1


# API to write to the output file.
# During testing, data written can be accessed via the data() method.
class OutputStream:
    def __init__(self):
        self._data = []
    
    # Writes pair to output file.
    def write(self, data):
        self._data.append(data)
            
    # For testing, OutputStream data is saved in memory.
    def data(self):
        return self._data


# File 1:

# aaa: 1
# bbb: 5
# bbb: 3
# ccc: 2

# File 2:

# bbb: 9
# ccc: 10
# ddd: 11

# We want to merge the two files together to produce an output file where keys are still sorted. Consecutive pairs with the same key in the output are merged, by summing up their values. e.g. merging the files above produces the output:

# [["aaa", 1], ......]
# [["bbb", 4]........]

# {

#     "aaa": 1
#     "bbb": 4
# }


# aaa: 1
# bbb: 17
# ccc: 12
# ddd: 11

from collections import defaultdict

# Implement this:
def merge_input_files(input_1: InputStream, input_2: InputStream, output: OutputStream):
    
    # Handle error case here 

    hashtable = defaultdict(int)

    input1 = []

    # t: O(N)
    # s: O(N)

    while input_1.is_valid():
        key, value = input_1.read() if input_1.read() != None else ["", 0]
        if key not in hashtable:
            input1.append([key, value]) 
        
        if  key in hashtable:
            hashtable[key] += value
        else:
            hashtable[key] = value 
        
        print("Key, Value, hashtable ", key, value, hashtable)

        input_1.next()
    
    input2 = []
    while input_2.is_valid():
        key, value = input_2.read() if input_2.read() != None else ["", 0]
        if key not in hashtable:
            input2.append([key, value])

        if key in hashtable:
            hashtable[key] += value
        else:
            hashtable[key] = value
        
        input_2.next()
    

    output = OutputStream()

    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(input1) and ptr2 < len(input2):
        key1 = input1[ptr1][0]
        key2 = input2[ptr2][0]

        value1 = hashtable[key1]
        value2 = hashtable[key2]
        
        if key1 < key2:
            output.write([key1, value1])
            ptr1 += 1
        elif key1 > key2:
            output.write([key2, value2])
            ptr2 += 1
        else:
            output.write([key1, value1])
            ptr1 += 1
            ptr2 += 1 
    

    while ptr1 < len(input1):
        key1 = input1[ptr1][0]
        value1 = hashtable[key1]
        output.write([key1, value1])
        ptr1 += 1
    
    while ptr2 < len(input2): 
        key2 = input2[ptr2][0]
        value2 = hashtable[key2]
        output.write([key2, value2])
        ptr2 += 1
    
    return output 

inp1 = InputStream([
    ("aaa", 1),
    ("bbb", 5),
    ("bbb", 3),
    ("ccc", 2),
])

inp2 = InputStream([
    ("bbb", 9),
    ("ccc", 10),
    ("ddd", 11),
    ("eee", 7)
])

output = OutputStream()
result = merge_input_files(inp1, inp2, output)._data
print(result)
assert result == [["aaa", 1], ["bbb", 17], ["ccc", 12], ["ddd", 11], ["eee", 7]] 