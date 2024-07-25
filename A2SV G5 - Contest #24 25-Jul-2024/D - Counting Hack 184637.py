# Problem: D - Counting Hack - https://codeforces.com/gym/534160/problem/D

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
    n = I()
    li = IL()
    
    visited = set()
    
    right = [0]*(n+1)
    
    for i in range(n-1,-1,-1):
        if li[i] not in visited:
            visited.add(li[i])
            right[i+1] = 1
            visited.add(li[i])
            
    for i in range(1,len(right)):
        right[i] += right[i-1]
        
    visited.clear()
    res = 0
    
    for i in range(n):
        if li[i] not in visited:
            res+=right[-1] - right[i]
            visited.add(li[i])
            
    return res

# t = 1
t = int(input())
for _ in range(t):
    print(solve())





