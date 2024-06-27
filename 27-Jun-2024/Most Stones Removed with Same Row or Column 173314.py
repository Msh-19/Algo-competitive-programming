# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self,size):
        self.parent = {i:i for i in range(size)}
        self.size = [1]*size

    def find(self, x):
        if x!= self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self,x,y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.parent[parentX] > self.size[parentY]:
                self.parent[parentY] = parentX
                self.size[parentX] += self.size[parentY]
            else:
                self.parent[parentX] = parentY
                self.size[parentY] += self.size[parentX]

    def connected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        u = UnionFind(n)


        X = {}
        Y = {}
        count = 0
        for i,(x,y) in enumerate(stones):
            if x in X:
                u.Union(i,X[x])
            else:
                X[x] = i
            if y in Y:
                u.Union(i,Y[y])
            else:
                Y[y] = i
        
        parents = len({u.find(i) for i in range(n)})
        return n - parents
