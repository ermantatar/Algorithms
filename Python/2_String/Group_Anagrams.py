from ast import List
import collections
class Solution:
    def group_anagrams(self, strs: List[str])-> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
    # t: O(NKlogK), where N = the length of strs, K is the max length of string in N strings.
    # s: O(NK) total information saved in the ans

    def group_anagrams(self, strs: List[str])-> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    # t: O(NK)
    # s: O(NK)