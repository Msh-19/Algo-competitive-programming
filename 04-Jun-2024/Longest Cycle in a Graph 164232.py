# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.result = -1
        visited = [False] * len(edges)
        print(visited)
        def dfs(node,dist):
            
            visited[node] = True 
            neighbour = edges[node]
            if neighbour != -1 and not visited[neighbour]:
                dist[neighbour] = dist[node] + 1 
                dfs(neighbour,dist) 
            
            elif neighbour != -1  and neighbour in dist:
                self.result = max(self.result,dist[node]- dist[neighbour]+1)


        for i in range(len(edges)):
            if not visited[i]:
                dist = {i : 1 }
                dfs(i,dist)

        return self.result