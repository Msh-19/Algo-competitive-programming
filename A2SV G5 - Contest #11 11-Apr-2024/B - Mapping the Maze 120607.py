# Problem: B - Mapping the Maze - https://codeforces.com/gym/515998/problem/B

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
    n,k = IL()
    degree = [0 for i in range(n)]
    for i in range(k):
        r,c = IL()
        r -= 1
        c -= 1
        
        degree[r] += 1
        degree[c] += 1
        
    count = Counter(degree)
    
    if count[2] == n:
        return "ring topology"
    elif count[1] == 2 and count[2] == (n-2):
        return "bus topology"
    elif count[1] == n-1 and count[n-1] == 1:
        return "star topology"
    else:
        return "unknown topology"
        


t = 1
# t = int(input())
for _ in range(t):
    print(solve())