# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

n = int(input())

count = 0

if n%2 !=0:
    count +=1
if n == 1:
    print(1)
else:
    while n!=1:
        n = n//2
        if n%2 != 0:
            count += 1
    print(count)