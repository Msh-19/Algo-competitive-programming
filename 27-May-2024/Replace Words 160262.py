# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word):
        res = []
        curr= self.root
        for c in word:
            if c not in curr.children:
                return word
            curr = curr.children[c]
            res.append(c)
            if curr.isEnd == True:
                return "".join(res)
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        return " ".join([trie.search(x) for x in sentence.split()])