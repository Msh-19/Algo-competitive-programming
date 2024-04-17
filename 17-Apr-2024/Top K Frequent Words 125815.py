# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        clist = Counter(words)
        maxfreq = 0
        maxlist = []
        coup = []
        for i,j in clist.items():
            coup.append((-j,i))

        heapify(coup)
        res = []
        for i in range(k):
            res.append(heappop(coup)[1])
        return res