# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [0]*n
        self.secret = [False]*n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if self.size[parentX] > self.size[parentY]:
                self.parent[parentY] = parentX
                
            elif self.size[parentY] > self.size[parentX]:
                self.parent[parentX] = parentY
                
            else:
                self.parent[parentY] = parentX
                self.size[parentX] += self.size[parentY]

    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def reset(self,x):
        self.parent[x] = x
        self.size[x] = 0

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])

        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))

        graph = UnionFind(n)
        graph.union(firstPerson, 0)

        for t in same_time_meetings:
            for x, y in same_time_meetings[t]:
                graph.union(x, y)

            for x, y in same_time_meetings[t]:
                if not graph.connected(x, 0):
                    graph.reset(x)
                    graph.reset(y)

        return [i for i in range(n) if graph.connected(i, 0)]