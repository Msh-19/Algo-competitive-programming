# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        parents = [set() for _ in range(n)]
        indegrees = [0] * n

        for par, cur in edges:
            graph[par].append(cur)
            parents[cur].add(par)
            indegrees[cur] += 1
        
        queue = deque()

        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()

            for neigh in graph[cur]:
                parents[neigh].update(parents[cur])
                indegrees[neigh] -= 1

                if indegrees[neigh] == 0:
                    queue.append(neigh)
        
        return [sorted(list(nodes)) for nodes in parents]