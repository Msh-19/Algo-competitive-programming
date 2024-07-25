# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    count = 0
    
    for i in range(len(li)-1):
        if li[i] != 0:
            count += li[i]
        elif count != 0 and li[i] == 0:
            count += 1
    print(count)