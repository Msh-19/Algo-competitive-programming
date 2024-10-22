# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dis = [0]*n
        dis[start] = 1

        for _ in range(n-1):
            updated = False
            for i,(u,v) in enumerate(edges):
                if dis[u] * succProb[i] > dis[v]:
                    dis[v] = dis[u] * succProb[i]
                    updated = True
                if dis[v] * succProb[i] > dis[u]:
                    dis[u] = dis[v] * succProb[i]
                    updated = True
            if not updated:
                break

        return dis[end]