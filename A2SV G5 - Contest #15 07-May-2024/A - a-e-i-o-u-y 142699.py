# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

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
    vowels = ("a", "e", "i", "o", "u", "y")
    
    n = int(input()) 
    s = input().strip()  
    
    wr = []
    for i in range(n):
        wr.append(s[i])
        
        if i>0 and s[i] in vowels and s[i-1] in vowels:
            wr.pop()
            
            
    return ''.join(wr)
            

t = 1
# t = int(input())
for _ in range(t):
    print(solve())


