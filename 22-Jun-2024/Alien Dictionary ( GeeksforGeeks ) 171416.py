# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import deque

class Solution:
    def findOrder(self,dict, N, K):
        graph = [[] for _ in range(k)]
        indegree = [0]*k
        
        for i in range(n-1):
            word1, word2 = dict[i],dict[i+1]
            
            for ch1, ch2 in zip(word1,word2):
                if ch1 == ch2:
                    continue
                
                ch1 = ord(ch1) - ord("a")
                ch2 = ord(ch2) - ord("a")
                graph[ch1].append(ch2)
                indegree[ch2] += 1
                break
        queue = deque()
        for i in range(k):
            if indegree[i] == 0:
                queue.append(i)
                
        result = []
        while queue:
            cur = queue.popleft()
            ch = chr(cur+ ord("a"))
            result.append(ch)
            
            for neigh in graph[cur]:
                indegree[neigh]-=1
                
                if indegree[neigh] == 0:
                    queue.append(neigh)
                    
        return "".join(result)