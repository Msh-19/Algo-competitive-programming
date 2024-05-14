# Problem: B - Instructions - https://codeforces.com/gym/523525/problem/B

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
    dp = [0]*n
    for i in range(n-1,-1,-1):
        if i+li[i] < n:
            dp[i] = li[i] + dp[i+li[i]]
        else:
            dp[i] = li[i]
    
    return max(dp)
# t = 1
t = int(input())
for _ in range(t):
    print(solve())