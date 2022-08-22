from typing import List


class Solution:
    # t: O(|E| + |V|)
    # s: O(|E| + |V|)
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i: [] for i in range(num_courses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        output = []
        seen = set()
        taken_courses = set()
        
        
        def dfs(crs):
            
            if crs in seen:
                return False 
        
            if crs in taken_courses:
                return True 
            
            seen.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False 
            seen.remove(crs)
            
            # successful take this course and sign it. 
            taken_courses.add(crs)
            output.append(crs)
            return True 
        
        
        
        for c in range(num_courses):
            if dfs(c) == False:
                return [] 
        return output




        
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        result = [0] * num_courses
        if num_courses == 0:
            return result

        if not prerequisites:
            result = [i for i in range(num_courses)]
            return result

        indegree = [0] * num_courses
        zero_degree = deque()
        for pre in prerequisites:
            indegree[pre[0]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_degree.append(i)
        if not zero_degree:
            return []

        index = 0
        while zero_degree:
            course = zero_degree.popleft()
            result[index] = course
            index += 1
            for pre in prerequisites:
                if pre[1] == course:
                    indegree[pre[0]] -= 1
                    if indegree[pre[0]] == 0:
                        zero_degree.append(pre[0])

        if any(i for i in indegree): 
            return []
            
        return result



        
