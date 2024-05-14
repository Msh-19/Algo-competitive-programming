# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

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
    n, a, b, c = map(int, input().split())
    
    dp = {}
    dp[0] = 0
    for i in range(1,n+1):
        dp[i] = -1
        if i >= a and dp[i - a] != -1:
            dp[i] = max(dp[i], dp[i - a] + 1)
        if i >= b and dp[i - b] != -1:
            dp[i] = max(dp[i], dp[i - b] + 1)
        if i >= c and dp[i - c] != -1:
            dp[i] = max(dp[i], dp[i - c] + 1)
    return dp[n]
t = 1
# t = int(input())
for _ in range(t):
    print(solve())


# import sys, threading

# input = lambda: sys.stdin.readline().strip()

# def main():
#     n,a,b,c= map(int,input.split())
#     li = []
#     li.append(a,b,c)
#     memo = {}
#     def recur(n,parts):
#         if n == 0:
#             return
#         if memo[n,parts] not in memo:
#             memo[n,parts] = recur(n-li[])
    
# if __name__ == '__main__':
    
#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()


