# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self,pts):
        self.parent = {}
        for i in range(len(pts)):
            self.parent[i] = None

    # this is quite confusing needs more improvement
    def find(self, n1):
        # could be implemented in 
        # def find(self, x):
        # if x != self.parent[x]:
        #     self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]

        while self.parent[n1] is not None:
            n1 = self.parent[n1]
        return n1

    def Union(self,n1,n2):
        rootn1 = self.find(n1)
        rootn2 = self.find(n2)
        if rootn1 == rootn2:
            return False
        self.parent[rootn2] = rootn1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_dist(points):
            lst = []
            for i in range(len(points)):
                x1,y1 = points[i]
                for j in range(i+1,len(points)):
                    x2,y2 = points[j]
                    dist = abs(x1-x2) + abs(y1-y2)
                    lst.append((dist,i,j))
            lst.sort(key=lambda x:x[0])
            return lst
        lst = get_dist(points)
        u = UnionFind(points)
        total = 0

        for d, i, j in lst:
            if u.Union(i,j):
                total += d
        return total