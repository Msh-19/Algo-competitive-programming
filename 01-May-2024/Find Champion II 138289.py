# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        indegree = set()
        outdegree = set()
        for i in range(len(edges)):
            if edges[i][0] not in outdegree:
                indegree.add(edges[i][0])
            indegree.discard(edges[i][1])
            outdegree.add(edges[i][1])
        if n - len(outdegree) > 1:
            return -1
        if n == 1:
            return 0
        
        return list(indegree)[0] 
