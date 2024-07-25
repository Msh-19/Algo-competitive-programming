# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

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

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

def solve():
    op = int(input())
    st = list(S())
    dsu = UnionFind(2*op)
       
    stack = []
    stack.append((st[0],0))
    
    for i in range(1,(2*op)):
        if st[i] == "(":
            stack.append((st[i],i))
            
        elif st[i] == ")":
            idx = stack.pop()[1]
            dsu.unite(i,idx)
            if idx-1 >= 0 and st[idx-1]== ")":
                dsu.unite(idx,idx-1)
                
    ans = set()
    for i in range(2*op):
        ans.add(dsu.find(i))
        
    return len(ans)
                
                
                
# t = 1
t = int(input())
for _ in range(t):
    print(solve())


