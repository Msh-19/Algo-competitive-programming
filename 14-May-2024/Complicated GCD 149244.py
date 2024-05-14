# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

import sys
from math import gcd
def input():
    return sys.stdin.readline().strip()

a, b = input().split()

if a == b:
    print(a)
else:
    print(1)