class Solution:
    # t: O(|E| + |V|)
    # s: O(|E| + |V|)
    def canFinish(self, num_courses, prerequisites):

        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        visited = [False] * num_courses
        path = [False] * num_courses

        for course in range(num_courses):
            if self.isCyclic(course, courseDict, visited, path):
                return False 
        return True 

    
    def isCyclic(self, course, courseDict, visited, path):

        # 1) bottom-cases 
        if visited[course]:
            # this node has been checked, no cycle would be formed with this node.
        
        if path[course]:
            # came accross a marked node on the path, cyclic! 
            return True
        
        # 2). postorder DFS on the children nodes
        # mark the node in the path
        path[course] = True 

        ret = False 
        # postorder DFS, to visit all its children first.
        for child in courseDict[course]:
            ret = self.isCyclic(child, courseDict, visited, path)
            if ret:
                break 
        
        # 3). after the visits of children, we come back to process the node itself
        # remove the node from the path
        path[currCourse] = False

        # Now that we've visited the nodes in the downstream,
        #   we complete the check of this node.
        checked[currCourse] = True
        return ret
