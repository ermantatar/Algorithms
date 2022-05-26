class Solution:
    def sequenceReconstruction(self, nums, sequences):
        graph = defaultdict(list)
        in_degree_counts = defaultdict(int)

        for seq in sequences:
            for i in range(1, len(seq)):
                graph[seq[i-1]].append(seq[i])
                in_degree_counts[seq[i]] += 1
        

        # the 1st num must have 0 incoming edge
        if in_degree_counts[0] > 0:
            return False 
        
        stack = [nums[0]]
        i = 1

        while stack:
            node = stack.pop()
            for child in graph[node]:
                in_degree_counts[child] -= 1
                if not in_degree_counts[child]:
                    # return false 
                    # if there are any other nodes with 0 incoming edges
                    # or the node with 0 incoming edges != nums[i]
                    if stack or child != nums[i]:
                        return False
                    stack.append(child)
                    i += 1
        
        return i == len(nums)
