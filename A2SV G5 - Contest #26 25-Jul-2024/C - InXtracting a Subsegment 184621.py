# Problem: C - InXtracting a Subsegment - https://codeforces.com/gym/537362/problem/C

n,k = map(int,input().split())

li = list(map(int,input().split()))

if k == 1:
    print(min(li))

elif k == 2:
    print(max(li[0],li[n-1]))
else:
    print(max(li))