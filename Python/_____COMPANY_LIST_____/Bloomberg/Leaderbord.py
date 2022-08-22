class Leaderboard:

    """
    BRUTE - FORCE 
    """

    # O(NlogN) for top func, others O(1) operations
    # O(N)
    def __init__(self):
        self.scores = defaultdict()
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId]+=score

    def top(self, K: int) -> int:
        values = [v for _, v in sorted(self.scores.items(), key=lambda x: x[1])]
        values.sort(reverse = True)
        total, i = 0, 0
        while i < K:
            total += values[i]
            i += 1
        
        return total 
        
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0



    """
    PRIORITY QUEUE APPROACH
    """
     
    # We don't have a way to construct a reverse SortedDict in Python and hence, we negate the scores before adding them to the dict 
    # (TreeMap like data structure) so that the normal in-order traversal would give us the scores in the reverse order i.e. descending order.


    # t: O(K) + O(NlogK), K here size of heap, and it takes O(size) to construct heap data structure, rest of the N-K elements * extrac_min and add operations NlogK
    def top(self, K:int) -> int:
        # this will be min-heap default in python
        heap = []

        for val in self.scores.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
        
        total = 0
        while heap:
            total += heapq.heappop(heap)
        
        return total 


"""
SORTED_DICT (balanced binary search tree)
"""

# All operations become O(logN)

from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:

        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with 
        # key as the score and value as the number of players that have
        # that score.     
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1    
            
            newScore = preScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
        
    def top(self, K: int) -> int:
        count, total = 0, 0;

        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times): 
                total += -key;
                count += 1;
                
                # Found top-K scores, break.
                if count == K:
                    break;
                
            # Found top-K scores, break.
            if count == K:
                break;
        
        return total;

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId];


        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)