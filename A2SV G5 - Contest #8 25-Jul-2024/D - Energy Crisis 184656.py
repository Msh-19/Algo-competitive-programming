# Problem: D - Energy Crisis - https://codeforces.com/gym/511242/problem/D

def check(arr, k, mid):
    total_transferred = 0
    for energy in arr:
        if energy > mid:
            total_transferred += (energy - mid) * (1 - k / 100)
        elif energy < mid:
            total_transferred -= (mid - energy)
    return total_transferred >= 0

def max_equal_energy(arr, k):
    low = 0
    high = max(arr)
    precision = 1e-6

    while high - low > precision:
        mid = (low + high) / 2
        if check(arr, k, mid):
            low = mid
        else:
            high = mid

    return low


n, k = map(int, input().split())
arr = list(map(int, input().split()))


print(max_equal_energy(arr, k))
