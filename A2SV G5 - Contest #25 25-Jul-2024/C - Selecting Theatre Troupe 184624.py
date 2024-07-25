# Problem: C - Selecting Theatre Troupe - https://codeforces.com/gym/535749/problem/C

from math import comb as c

bo,gi,t = map(int, input().split())

ans = 0

for i in range(4,t):
    if bo>= i and gi >= t - i:
        ans+= c(bo,i)*c(gi,t-i)

print(ans)