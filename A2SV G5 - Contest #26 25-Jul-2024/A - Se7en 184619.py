# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

t = int(input())

for _ in range(t):
    num = int(input())
    k = num%7
    
    if (num%10) < k:
        print(num-k+7)
    else:
        print(num-k)