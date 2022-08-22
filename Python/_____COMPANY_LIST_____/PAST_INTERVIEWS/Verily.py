# [3, 2, 1, 5, 2, 3], 3 => 2


def lookForTargetIndex(nums, target):
   if not nums:
    return 0 
   l, r = 0, len(nums)-1
   index = 0
  
   while l <= r:
     m = l + (r - l) // 2
#      print(l, m, r)
    
     if nums[m] < target:
       l = m + 1
     elif nums[m] > target:
       r = m - 1
     else:
       return m
#       index = target 
   
#      print("looping: ")
   return index
  
def searchForNumber(nums, target):
  target_count = 0
  index = lookForTargetIndex(nums, target)
  l = index
  r = index + 1
#   print("INDEX: ", r)
  while (nums[l] == target):
    target_count += 1
    l-=1
      
  while (nums[r] == target):
    target_count += 1
    r += 1
     
  return target_count

# def searchForNumber(nums, target):
    
#     target_count = 0
#     index = lookForTargetIndex(nums, target)
    
#     for i in range(index, len(nums)):
#       if nums[i] == target:
#         target_count += 1
    
#     return target_count
  
  
  
print(searchForNumber([1, 2, 2, 3, 3, 5], 3), 2)
print(searchForNumber([1, 2, 2, 3, 3, 5], 1), 1)
print(searchForNumber([1, 2, 2, 3, 3, 5], 2), 2)
print(searchForNumber([3, 3], 0), 0)


  
 
      
   
    
  #### 2nd Round #####

  class LogEntry:
  def __init__(self, requestId, timestamp, isStart):
    self.requestId = requestId
    self.timestamp = timestamp
    self.isStart = isStart

TIMEOUT = 3

import heapq 

def logHasTimeout(log):
  
  heap = []
  heapq.heapify(heap)
    
  queue = collections.deque()
  
 
    
    
  for log_entry in log:
    print(log_entry.requestId)
    # Your code here! Feel free to define new classes or restructure this code as needed.
    
    if queue and log_entry.timestamp - queue[0][0] >= 3:
      return True 
      # queue.popleft(heap)
    
    
    
    if not log_entry.isStart == False:
      log = [log_entry.timestamp, log_entry.requestId, log_entry_isStart]
      queue.append(log)
    else:
      if queue and queue[0][1] == log_entry.requestId:
        queue.popleft()
     
  return False


[ [0, A], [6, C]  ]
    
# Graphical representation of the log
# ID: C                               (-------)
# ID: B            (-----------------------)
# ID: A       (-------)
# Time:       0   1   2   3   4   5   6   7   8
exampleLog = [
  LogEntry("X", 0, True),
  LogEntry("A", 1, True),
  LogEntry("A", 2, False),
  LogEntry("C", 6, True),
  LogEntry("C", 8, False)
]

print(logHasTimeout(exampleLog))



### 3rd Round ####

"""
graph = {
  'A': ['B', 'D'],
  'B': ['C', 'A'],
  'C': ['D', 'B'],
  'D': ['A', 'C'],
}

  A — B
  |   |
  D — C 
 
 
 A - B - C - D -
 
 O(|V| + |E|)
 O(|V| + |E|)
 
 o-o-o-o-o-o-o-o-
 
 E = V - 1
 
 
[A, B, C, D]
[A, D, C, B]
"""


graph = {
  'A': ['B', 'D'],
  'B': ['C', 'A'],
  'C': ['D', 'B'],
  'D': ['A', 'C'],
}

def traverse(graph):
  
  if not graph:
    return []
  
  visited = set()
  
  def dfs(node, path, destination):
   
    
    
    visited.add(node)
    print("Curr, Path, Dest, Visited: ", node, path, destination, visited)
    # D 
    for neighbor in graph[node]:
      if neighbor not in visited:
          path = dfs(neighbor, path + [neighbor], destination)
      else:
        if neighbor == destination:
          break 
          
    return path
          
  path = ["A"]
  # visited.add("A")
  return dfs("A", path, "A")
  
 

print(traverse(graph))
  
  
  
  
