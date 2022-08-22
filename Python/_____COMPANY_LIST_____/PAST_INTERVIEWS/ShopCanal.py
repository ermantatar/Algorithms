"""
Isomorphism is a property of two words. Write a function that accepts two words
and returns whether the words are isomorphic or not. Two words are called
isomorphic if the letters in one word can be remapped to get the other word.
Remapping a letter means replacing all occurrences of it with another letter.
The ordering of the letters remains unchanged. No two letters may map to the
same letter. A letter may map to itself.

mom <-> mom TRUE
mom <-> dad TRUE
mom <-> dog FALSE
dog <-> mom FALSE
dog <-> cat FALSE
mom <-> mmo
happy <-> farro
hey <-> hi NO

aab -> ano: NOT ISOMORPHIC
"""

# {a: 2, b: 1, c: 1} ---- {x: 2, y: 1, z: 1}

# d o d <-> m o m

# d o g <-> m o m

# d d o d -> m o m m

# ddodoo -> mommoo 

from collections import defaultdict
from typing import Optional

def isIsomorphic(s1: Optional[str], s2: Optional[str]) -> bool:
    # Size check and Null Checks 
    if not s1 and not s2:
      return True
    elif not s1 or not s2 or (len(s1) != len(s2)):
      return False 
    
    hash_table_s1 = defaultdict(int)
    for c in s1:
      hash_table_s1[c] = hash_table_s1.get(c, 0) + 1
    
    hash_table_s2 = defaultdict(int)
    for c in s2:
      hash_table_s2[c] = hash_table_s2.get(c, 0) + 1
    
    mapping = {}
    i = 0
    for i in range(len(s1)):
      if hash_table_s1[s1[i]] == hash_table_s2[s2[i]]:
        if s1[i] in mapping and mapping[s1[i]] == s2[i]:
          continue
        elif s1[i] in mapping and mapping[s1[i]] != s2[i]:
          return False
        mapping[s1[i]] = s2[i]
      else:
        return False
    
    return True 

# print(isIsomorphic("mom", "mom"))
# print(isIsomorphic("dad", "dad"))
# print(isIsomorphic("mom", "dog"))
# print(isIsomorphic("dog", "mom"))
# print(isIsomorphic("dog", "mom"))
# print(isIsomorphic("ddodoo","mommoo"))
# print(isIsomorphic("dog",""))


def is_partialy_isomorphic(s1, s2):
  mapping = {}
  for i in range(len(s1)):
    if s1[i] in mapping:
      if mapping[s1[i]] != s2[i]:
        return False
      continue
    mapping[s1[i]] = s2[i]
  return True

def is_isomorphic(s1, s2):
  return is_partialy_isomorphic(s1, s2) and is_partialy_isomorphic(s2, s1)

print(is_isomorphic("mom", "mmm"))



def is_half_isomorphic(s1, s2):
  if len(s1) != len(s2):
    return False
  mapping = {}
  for i in range(len(s1)):
    if s1[i] in mapping:
      if mapping[s1[i]] != s2[i]:
        return False
      continue
    mapping[s1[i]] = s2[i]
  return True

def is_isomorphic(s1, s2):
  return is_half_isomorphic(s1, s2) and is_half_isomorphic(s2, s1)

print(is_isomorphic("mom", "mmm"))

assert is_isomorphic('mom', 'dad') is True
assert is_isomorphic('dad', 'lol') is True
assert is_isomorphic('dog', 'cat') is True

assert is_isomorphic('mom', 'dog') is False
assert is_isomorphic('dog', 'mom') is False
assert is_isomorphic('dad', 'dog') is False
assert is_isomorphic('dog', 'dad') is False
assert is_isomorphic('dog', 'hi') is False

assert is_isomorphic('yaday', 'dayad') is True
assert is_isomorphic('lala', 'aaaa') is False
assert is_isomorphic('lalas', 'dedee') is False

print("all good")