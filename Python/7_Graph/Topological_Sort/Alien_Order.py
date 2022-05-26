class Solution:
    def alienOrder(self, words: List[List[int]]) -> str:
        
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Create directed edge between two characters, adj[x]:{b} means a -> b  
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break 
            
            visit = {} # False: Visited, True: It is currently on the path 
            res = []

            def dfs(c):
                # neetcode


            



            