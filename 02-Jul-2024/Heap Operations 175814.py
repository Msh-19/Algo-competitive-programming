# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import heapify, heappop, heappush
import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
heap = []
result = []

for _ in range(n):
    oper = list(input().split())

    if oper[0] == "insert":
        heappush(heap, int(oper[1]))
        result.append("insert " + oper[1])
    elif oper[0] == "getMin":
        val = int(oper[1])
        while heap and heap[0] < val:
            heappop(heap)
            result.append("removeMin")

        if not heap or heap[0] > val:
            heappush(heap, val)
            result.append("insert " + oper[1])

        result.append("getMin " + oper[1])
    else:
        if heap:
            heappop(heap)
        else:
            result.append("insert " + str(int(1e9)))

        result.append("removeMin")

print(len(result))
for line in result:
    print(line)
