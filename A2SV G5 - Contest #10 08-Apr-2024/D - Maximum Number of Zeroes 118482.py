# Problem: D - Maximum Number of Zeroes - https://codeforces.com/gym/514644/problem/D

from sys import stdin
from math import gcd
def input(): return stdin.readline().strip()

from collections import Counter

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = Counter()
ans = 0

for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            ans += 1
    else:
        x = b[i]//(gcd(abs(a[i]), abs(b[i])))
        y = a[i]//(gcd(abs(a[i]), abs(b[i])))
        
        if b[i] <0:
            x*=-1
            y*=-1
        elif b[i] == 0 and a[i] < 0:
            y*= -1
        count[(x,y)] += 1
        
if len(count) == 0:
    print(ans)
else:
    print(ans+max(count.values()))