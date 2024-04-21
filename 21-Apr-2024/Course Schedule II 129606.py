# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, p: List[List[int]]) -> List[int]:
        topsort = []
        q = deque()

        list_ = defaultdict(list)
        indegree = defaultdict(lambda:0)
        for edge in p:
            indegree[edge[0]]+=1
            list_[edge[1]].append(edge[0])

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while len(q)>0:
            curr = q.popleft()
            topsort.append(curr)
            for nodes in list_[curr]:
                indegree[nodes]-=1
                if indegree[nodes]==0:
                    q.append(nodes)

        return topsort if len(topsort) == numCourses else []