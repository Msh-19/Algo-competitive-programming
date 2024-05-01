# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys
t = int(input())

def input():
    return sys.stdin.readline().strip()

for _ in range(t):
    
    nu = int(input())
    if nu == 1:
        print(3)
        continue
    i = 1
    flag =False
    while i<nu:
        if i^nu and i&nu:
            print(i)
            flag = True
            break
        i<<=1
        
    if flag == False:
        print(nu|1)