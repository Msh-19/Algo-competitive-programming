# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B


import sys

def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def IL(): return list(map(int, input().split()))
def S(): return input()
def SL(): return input().split()

def solve():
    n,k = map(int, input().split())
    
    fron = False
    back = False
    for _ in range(n):
        s,e = map(int,input().split())
        if s==k:
            fron = True
        if e == k:
            back = True
    if fron and back:
        return "YES"
    else:
        return "NO"

# t = 1
t = int(input())
for _ in range(t):
    print(solve())
