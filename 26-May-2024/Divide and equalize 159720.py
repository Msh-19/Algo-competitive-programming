# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import math
import sys
from collections import Counter

def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def IL(): return list(map(int, input().split()))
def S(): return input()
def SL(): return input().split()


def primes(num):
    facts = Counter()
    i = 2
    while i * i <= num:
        while num % i == 0:
            facts[i] += 1
            num //= i
        i += 1
    if num > 1:
        facts[num] += 1
    return facts

def solve():
    n = I()
    arr = IL()
    counts = Counter()
    
    for i in range(n):
        counts.update(primes(arr[i]))
    
    for num, count in counts.items():
        if count % n != 0:
            print("NO")
            return

    print("YES")

# t = 1
t = int(input())
for _ in range(t):
    solve()


