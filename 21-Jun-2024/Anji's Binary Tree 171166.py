# Problem: Anji's Binary Tree - https://codeforces.com/contest/1900/problem/C

from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    graph = defaultdict(list)
    
    for i in range(1,n+1):
        graph[i].append(s[i-1])
        a = list(map(int,input().split()))
        for num in a:
            graph[i].append(num)
            
    stack = []
    stack.append(1)
    ans = []
    dic_ = defaultdict(int)
    
    while stack:
        curr = stack.pop()
        if graph[curr][1] == 0 and graph[curr][2] ==0:
            ans.append(dic_[curr])
        for idx,neigh in enumerate(graph[curr]):
            add = 0
            if neigh!=0 and idx!=0:
                if graph[curr][0]!="L" and idx == 1:
                    add+=1
                if graph[curr][0]!="R" and idx == 2:
                    add+=1
                stack.append(neigh)
                dic_[neigh] = dic_[curr]+add
    print(min(ans))
    