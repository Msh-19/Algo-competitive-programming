# Problem: A - Duale String - https://codeforces.com/gym/520688/problem/A

from collections import defaultdict, Counter, deque
import sys
 
def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def IL(): return list(map(int, input().split()))
def S(): return input()
def SL(): return input().split()
 
 
 
def solve():
    s = list(input())
    if len(s)%2 != 0:
        return "NO"
    mid = len(s)//2 
    if s[:mid] == s[mid:]:
        return "YES"
    else:
        return "NO"
        
# t = 1
t = int(input())
for _ in range(t):
    print(solve())