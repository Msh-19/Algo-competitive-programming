# Problem: A - Flag Checker - https://codeforces.com/gym/515998/problem/A

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
    n,m = IL()
    grid = []
        
    for j in range(n):
        temp = input()
        for o in range(m-1):
            if temp[o] != temp[o+1]:
                return "NO"
        grid.append(temp)

    for k in range(1,n):
        if grid[k][0] == grid[k-1][0]:
            return "NO"

    return "YES"
            
            


t = 1
# t = int(input())
for _ in range(t):
    print(solve())