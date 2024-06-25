# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, n):
        self.parent = list(n)
        self.rank = [1] * len(self.parent)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        n = len(s)
        dsu = UnionFind(range(n))

        for i , j in pairs:
            dsu.union(i , j)
        
        counter = defaultdict(list)

        for j , ch in enumerate(s):
            heappush(counter[dsu.find(j)] , ch)
        
        ans  = []

        for k , w in enumerate(s):
            ans.append(heappop(counter[dsu.find(k)]))

        return "".join(ans)