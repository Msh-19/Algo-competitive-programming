# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

import sys


def input():
    return sys.stdin.readline().strip()


def minSteps(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2

    leftSteps = minSteps(arr, left, mid)
    rightSteps = minSteps(arr, mid + 1, right)

    if leftSteps == -1 or rightSteps == -1:
        return -1

    leftMin, leftMax = float('inf'), float('-inf')
    rightMin, rightMax = float('inf'), float('-inf')

    for i in range(left, mid + 1):
        leftMin = min(leftMin, arr[i])
        leftMax = max(leftMax, arr[i])

    for i in range(mid + 1, right + 1):
        rightMin = min(rightMin, arr[i])
        rightMax = max(rightMax, arr[i])

    if leftMin > rightMax:
        return 1 + leftSteps + rightSteps
    elif rightMin > leftMax:
        return leftSteps + rightSteps
    else:
        return -1


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    print(minSteps(arr, 0, n - 1))
