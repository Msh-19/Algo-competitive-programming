# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(int)

        for ch in words:
            bitw = 0
            for c in ch:
                bitw |= (1<<ord(c)-97)
            lookup[ch] = bitw

        def don_share(s,t):
            if lookup[s]&lookup[t]:
                return False
            return True

        max_ = 0
        for i in words:
            for j in words:
                if don_share(i,j):
                    max_ = max(max_,len(i)*len(j))

        return max_