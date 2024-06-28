# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size 
        self.m = [float("inf")] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def f(self):
        return self.m[self.find(1)]  

    def union(self, x, y, w):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            self.m[parentX] = min(self.m[parentX], w)
            return

        if self.size[parentX] > self.size[parentY]:
            self.parent[parentY] = parentX
            self.size[parentX] += self.size[parentY]
            self.m[parentX] = min(self.m[parentX], self.m[parentY], w)
        else:
            self.parent[parentX] = parentY
            self.size[parentY] += self.size[parentX]
            self.m[parentY] = min(self.m[parentY], self.m[parentX], w)

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = UnionFind(n + 1)  

        for road in roads:
            u, v, w = road
            d.union(u, v, w)

        return d.f()