# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    li = input()

    count = 0
    for i in range(n-1,-1,-1):
        if li[i] == ")":
            count +=1 
        else:
            break
        
    if count > n//2:
        print("Yes")
    else:
        print("No")