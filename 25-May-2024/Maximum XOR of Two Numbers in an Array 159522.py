# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None]*2
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        cur = self.root
        for i in range(32,-1,-1):
            v = 1 if (num &(1<<i))>0 else 0
            if not cur.children[v]:
                cur.children[v] = TrieNode()
            cur = cur.children[v]
    def findMax(self,num):
        res =0 
        cur = self.root
        for i in range(32,-1,-1):
            v = 1 if (num &(1<<i)) >0 else 0
            if cur.children[1-v]:
                res = res | 1<<i
                cur = cur.children[1-v]
            else:
                cur = cur.children[v]
        return res
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        ans = 0
        for num in nums:
            ans = max(ans, trie.findMax(num))
        return ans