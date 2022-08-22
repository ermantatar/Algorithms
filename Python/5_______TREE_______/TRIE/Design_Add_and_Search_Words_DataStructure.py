
class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.endOfWord = False
'''
Look for Big O:
https://leetcode.com/problems/design-add-and-search-words-data-structure/solution/
'''
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        
    # Implement a recursive function dfs, and send (0, self.root)
    # Index value sent to dfs, will determine current character at the string 
    # See if that character is equals to "." if not, go ahead and check if it is in children
    # If it is, move to that children, loop will go next char,
    # If char == "." and we will loop values of the current node children, then call dfs(i+1, child)
    # If anyone of them returns True we can return True, otherwise, we can return False

    # t: ... words: O(26 ^ M), O(M)for well defined words
    # s: ... words O(M), well defined words O(1)
    def search(self, word: str) -> bool:
        
        def dfs(string_start_idx, root):    
            
            curr = root
            
            for i in range(string_start_idx, len(word)):
                c = word[i]
                
                if c == ".":
                    # see posibilities of all childs, with dfs, sending +1 to string_start_idx
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.endOfWord
            
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)