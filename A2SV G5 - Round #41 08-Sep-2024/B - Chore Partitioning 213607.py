# Problem: B - Chore Partitioning - https://codeforces.com/gym/545013/problem/B

n,a,b = map(int,input().split())

li = list(map(int, input().split()))
li.sort()

if li[b-1] == li[b]:
    print(0)
    
else:
    print((li[b] - li[b-1]))