# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites: return [False] * len(queries)

        indegree = [0]*numCourses
        adj_list = defaultdict(list)

        for s, d in prerequisites:
            adj_list[s].append(d)
            indegree[d] +=1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        reqs = [set() for _ in range(numCourses)]
        while queue:
            curr = queue.popleft()
            for neighbor in adj_list[curr]:
                reqs[neighbor].update(reqs[curr],[curr])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: queue.append(neighbor)

        ans = []
        for first,second in queries:
            ans.append(first in reqs[second])

        return ans