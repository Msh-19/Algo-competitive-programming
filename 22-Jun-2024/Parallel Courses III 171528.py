# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for i in range(n)]
        prev = [0]*n
        indegree = [0]*n

        for a,b in relations:
            a-=1
            b-=1

            graph[a].append(b)
            indegree[b]+=1

        reqTime = -1
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            curTime = prev[cur] + time[cur]
            reqTime = max(reqTime,curTime)

            for neigh in graph[cur]:
                indegree[neigh]-=1
                prev[neigh] = max(prev[neigh],curTime)

                if indegree[neigh] == 0:
                    q.append(neigh)

        return reqTime