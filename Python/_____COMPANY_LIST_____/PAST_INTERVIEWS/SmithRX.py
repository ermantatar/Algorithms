from collections import defaultdict
# CONSTANTS
ACCOUNT_A = "A"
ACCOUNT_B = "B"

def solution(R, V):
    # write your code in Python 3.6
    if not R or not V:
        return []
    if len(R) != len(V): return []

    accounts = defaultdict(int)
    accounts[ACCOUNT_A] = 0
    accounts[ACCOUNT_B] = 0

    lowest = defaultdict(int)
    lowest[ACCOUNT_A] = 0
    lowest[ACCOUNT_B] = 0

    for recipient, amount in zip(list(R.upper()), V):
        sender = ACCOUNT_B if recipient == ACCOUNT_A else ACCOUNT_A

        # transfer 
        accounts[sender] = accounts.get(sender, 0) - amount
        lowest[sender] = min(lowest[sender], accounts[sender])

        accounts[recipient] = accounts.get(recipient, 0) + amount
        # check the lowest
    
    return [abs(lowest.get(ACCOUNT_A, 0)), abs(lowest.get(ACCOUNT_B, 0))]


# TESTS 

# Wrong Key (lowercase), C,D,E diff keys are ignored since assumptions made accordingly. 
assert solution("bAabA", [2,4,1,1,2]) == [2, 4]
# Only one key exist 
assert solution("BBBBB", [1,1,1,1,1]) == [5, 0]
# Average Cases
assert solution("BAABA", [2,4,1,1,2]) == [2, 4]

# Missing Input, N was assumed to be min 1, but I added this case anyways. 
assert solution("", [2,4,1,1,2]) == []
assert solution("BAB", []) == []

# Null Values 
assert solution(None, [2,4,1,1,2]) == []
assert solution("BAB", None) == []