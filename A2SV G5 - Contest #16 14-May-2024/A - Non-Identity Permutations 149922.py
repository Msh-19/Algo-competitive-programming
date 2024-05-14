# Problem: A - Non-Identity Permutations - https://codeforces.com/gym/523525/problem/A

from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import math
import sys

def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def IL(): return list(map(int, input().split()))
def S(): return input()
def SL(): return input().split()

t = int(input())
for _ in range(t):

    n = I()
    li = []
    res = []
    for i in range(n):
        li.append(i+1)
    

    for j in range(n):
        res.append(li[j-1])

    print(*res)
        




