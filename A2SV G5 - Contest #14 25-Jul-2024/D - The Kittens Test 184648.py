# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D

from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import math
import sys

def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def IL(): return list(map(int, input().split()))
def S(): return input()
def SL(): return input().split()

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.group = {i:[i + 1] for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] > self.size[root_y]:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.group[root_x].extend(self.group[root_y])
            else:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
                self.group[root_y].extend(self.group[root_x])
                
    def same(self, x, y):
        return self.find(x) == self.find(y)

def solve():
    n = I()
    uf = UnionFind(n)
    for _ in range(n-1):
        x,y = map(int,input().split())
        uf.unite(x-1,y-1)
        
    print(*uf.group[uf.find(1)])


t = 1
# t = int(input())
for _ in range(t):
    solve()


