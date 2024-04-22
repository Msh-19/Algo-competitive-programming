# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        waiting = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        res = []
        i = 0
        t = 0
        while i <len(tasks) or waiting:

            while i<len(tasks) and tasks[i][0] <= t:
                heappush(waiting, (tasks[i][1], tasks[i][2]))  
                i += 1
            if waiting:
                process,taskindex = heappop(waiting)
                t += process
                res.append(taskindex)

            else:
                t = tasks[i][0]

        return res

        