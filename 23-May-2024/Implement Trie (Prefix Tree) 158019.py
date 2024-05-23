# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur  = self.root
        for i in word:
            let = ord(i) - ord("a")
            if not cur.children[let]:
                cur.children[let] = TrieNode()
            cur = cur.children[let]
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        beg = self.root
        for i in word:
            let = ord(i) - ord("a")
            if not beg.children[let]:
                return False

            beg = beg.children[let]
        if beg.is_end == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        beg = self.root
        for i in prefix:
            let = ord(i) - ord("a")
            if not beg.children[let]:
                return False

            beg = beg.children[let]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)