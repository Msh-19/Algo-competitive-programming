# Problem: A - Shalamagando's  workout - https://codeforces.com/gym/517685/problem/A

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
    T = I()
    li = IL()
    ch = 0
    bi = 0
    back = 0
    for i in range(T):
        if i%3 == 0:
            ch += li[i]
        if i%3 == 1:
            bi += li[i]
        if i%3 == 2:
            back += li[i]
            
    if ch > bi and ch>back:
        return "chest"
    elif ch < bi and bi > back:
        return "biceps"
    else:
        return "back"        


t = 1
# t = int(input())
for _ in range(t):
    print(solve())