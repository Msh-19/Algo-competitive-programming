# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            le = ord(ch) - ord("a")
            if not cur.child[le]:
                cur.child[le] = TrieNode()
            cur = cur.child[le]

        cur.isEnd = True

    def bfs(self):
        q = deque()
        q.append((self.root, []))
        maxlen = 0
        res = ""
        while q:
            node, lett = q.popleft()
            for i in range(26):
                if node.child[i] and node.child[i].isEnd:
                    ch = chr(ord("a") + i)
                    q.append((node.child[i], lett + [ch]))
            if len(lett) > maxlen:
                maxlen = len(lett)
                res = lett

        return "".join(res)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        curr = Trie()
        for word in words:
            curr.insert(word)
        
        return curr.bfs()
