class Solution:
    # t: O(|E| + |V|)
    # s: O(|E| + |V|)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # map each course to prereq list
        preMap = {i : [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        
        seen = set()
        
        def dfs(course:int)->bool:
            
            if course in seen:
                return False # this schedule cannot be completed, cycle! 
            
            if preMap[course] == []:
                return True 
            
            # process the course 
            seen.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False # if one course can't be completed, then whole schedule can't be completed 
            
            seen.remove(course)
            preMap[course] = [] # to give a message that this course can be completed, don't calculate over and over again in the future. 
            return True 
        
        # The reason we loop here, instead of sending one node, graph might be disconnected, we might not reach all the nodes. 
        for course in range(numCourses):
            if dfs(course) == False:
                return False 
        return True 

    # 2nd way     
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