# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        par = {i:i for i in range(1,n+1)}
        res = [[]]
        def find(x):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]

        def union(x,y):
            px = find(x)
            py = find(y)
            if px == py:
                res[0] = [x,y]
            else:
                par[px] = py
        
        
        for i in range(len(edges)):        
            union(edges[i][0],edges[i][1])

        return res[0]