# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

from collections import Counter
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    li = list(map(int, input().split()))
    count = Counter(li)
    memo = {}
    def dp(ind):
        if ind <=0:
            return 0
        if ind in memo:
            return memo[ind]
        
        if ind not in memo:
            memo[ind] = max(count[ind]*ind+dp(ind-2),dp(ind-1))
            return memo[ind]
    print(dp(max(li)))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


