# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = [None for _ in range(26)]
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            let = ord(char) - ord("a")
            if not cur.children[let]:
                cur.children[let] = TrieNode()
            cur = cur.children[let]

        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root
        i = 0
        stack = []
        stack.append((cur,i))
        # DFS through the TRIE
        while stack:
            cur, ind = stack.pop()
            if len(word) == ind:
                if cur.isEnd:
                    return True
                continue
            if word[ind] == ".":
                for node in cur.children:
                    if node is not None:
                        stack.append((node,ind+1))
            else:
                let = ord(word[ind]) - ord("a")
                if not cur.children[let]:
                    continue
                stack.append((cur.children[let],ind+1))

        return False
                    

        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)