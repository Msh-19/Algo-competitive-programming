# Problem: E - Numbers on the Blackboard - https://codeforces.com/gym/514644/problem/E

from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import math
import sys

def input(): return sys.stdin.readline().strip()
# def I(): return int(input())
def IL(): return list(map(int, input().split()))
# def S(): return input()
# def SL(): return input().split()


def solve():
    n,k = map(int,input().split())
    a = IL()
    
    if a.count(a[0]) == n:
        return 0
    
    for x in a:
        if (x>=k and a[0] <=k) or (x<=k and a[0]>=k):
            return -1
        
    gcd = abs(k - a[0])
    for i in a:
        gcd = math.gcd(gcd,abs(k-i))
        
    ans = 0
    for i in a:
        ans += (abs(k-i)//gcd -1)
        
    return ans


# t = 1
t = int(input())
for _ in range(t):
    print(solve())