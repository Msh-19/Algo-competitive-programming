# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import math
import sys

def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def IL(): return list(map(int, input().split()))
def S(): return input()
def SL(): return input().split()


def solve():
    n, m = IL()
    
    parents = {i: i for i in range(1, n + 1)}
    mins = {i: i for i in range(1, n + 1)}
    maxs = {i: i for i in range(1, n + 1)}
    size = {i: 1 for i in range(1, n + 1)}
    
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        
        if rootX != rootY:
            if size[rootX] > size[rootY]:
                rootX, rootY = rootY, rootX
            parents[rootX] = rootY
            size[rootY] += size[rootX]
            mins[rootY] = min(mins[rootX], mins[rootY])
            maxs[rootY] = max(maxs[rootX], maxs[rootY])
    
    for _ in range(m):
        query = input().split()
        if query[0] == "union":
            x, y = map(int, query[1:])
            union(x, y)
        else:
            x = int(query[1])
            root = find(x)
            print(mins[root], maxs[root], size[root])

t = 1
# t = int(input())
for _ in range(t):
    solve()
