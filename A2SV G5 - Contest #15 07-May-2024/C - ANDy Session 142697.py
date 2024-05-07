# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

def maximize_AND(n, k, a):
    sums = 0
    for i in range(30,-1,-1):
        po = pow(2,i)
        
        p = 0
        for j in range(n):
            val = po&a[j]

            if val == 0:
                p+=1
                
        if p<=k:
            k -= p
            sums += po
            
    return sums

t = int(input())


for _ in range(t):

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(maximize_AND(n, k, a))
