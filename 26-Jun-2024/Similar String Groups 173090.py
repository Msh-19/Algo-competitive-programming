# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class DSU:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [1]*n
    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self,x,y):
        px,py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.rank[px] += self.rank[py]
            self.par[py] = px
        else:
            self.rank[py] += self.rank[px]
            self.par[px] = py

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        ls = len(strs)
        dsu = DSU(ls)

        for i in range(ls):
            for j in range(i+1,ls):

                if dsu.par[i] == dsu.par[j]:
                    continue
                diff = 0
                
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    dsu.union(i,j)
        
        for i in range(ls):
            dsu.find(i)

        return len(set(dsu.par))
