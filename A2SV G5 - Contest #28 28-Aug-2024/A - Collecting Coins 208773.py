# Problem: A - Collecting Coins - https://codeforces.com/gym/540354/problem/A

t = int(input())

for _ in range(t):
    a,b,c,n = map(int, input().split())
    
    val = max(a,b,c)
    
    d = abs(val - a) + abs(val - b) + abs(val-c)
    
    n= n - d
    if n < 0:
        print("NO")
    elif n%3 == 0:
        print("YES")
    else:
        print("NO")