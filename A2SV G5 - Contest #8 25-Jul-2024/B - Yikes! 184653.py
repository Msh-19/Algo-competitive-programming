# Problem: B - Yikes! - https://codeforces.com/gym/511242/problem/B

import bisect
m = int(input())
pi = list(map(int,input().split()))
n = int(input())
pi2 = list(map(int,input().split()))
cur = 0
pre = []
pre.append(0)
for i in range(len(pi)):
    cur+=pi[i]
    pre.append(cur)
for j in range(len(pi2)):
    print(bisect.bisect_left(pre, pi2[j]))
    
