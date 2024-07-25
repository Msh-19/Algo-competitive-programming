# Problem: C - Removal Hack - https://codeforces.com/gym/534160/problem/C

from collections import defaultdict
from sys import stdin


def input(): return stdin.readline().strip()

N = int(input())

child = defaultdict(list)
respect = [0]*N

root = 0

for ch in range(N):
    p, c = map(int, input().split())
    p -= 1
    respect[ch] = c
    if p == -2:
        root = ch
        continue
    child[p].append(ch)

stack = [root]

ans = []

while stack:
    v = stack.pop()
    ok = respect[v]
    for ch in child[v]:
        stack.append(ch)
        if respect[ch] == 0:
            ok = False
    if ok:
        ans.append(v + 1)
if not ans:
    print(-1)
else:
    print(*sorted(ans))