# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

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
    n,z = map(int,input().split())
    a= IL()
    
    maxval = float("-inf")
    
    for i in range(n):
        orr = a[i]|z
        anr = a[i]&z
        mx = max(orr,anr)
        
        maxval = max(maxval,mx)
    return maxval

# t = 1
t = int(input())
for _ in range(t):
    print(solve())


