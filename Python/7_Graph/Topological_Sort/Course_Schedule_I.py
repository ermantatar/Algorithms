class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        result = [0] * numCourses
        if numCourses == 0:
            return True
        
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        in_degree = [0] * numCourses 
        zero_in_queue = deque()
        
        dep = collections.defaultdict(list)
        
        
        for i in range(len(prerequisites)):
            pre = prerequisites[i]
            dep[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                zero_in_queue.append(i)
        
        if not zero_in_queue:
            return False 
        
        index = 0 
        while zero_in_queue:
            course = zero_in_queue.popleft()
            result[index] = course
            index += 1
            for neighbor in dep[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_queue.append(neighbor)
            
        
        if any(i for i in in_degree):
            return False 
        
        return True