# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # check for values where there is no outgoing from the node
        gr = [[] for _ in range(len(graph))]
        incoming = [0 for _ in range(len(graph))]
        queue = deque()
        res = []

        for r in range(len(graph)):
            for c in graph[r]:
                gr[c].append(r)
            incoming[r] = len(graph[r])

        for node in range(len(gr)):
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in gr[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        res.sort()
        return res


