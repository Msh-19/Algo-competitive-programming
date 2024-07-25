# Problem: E - Candies - https://codeforces.com/gym/535749/problem/E

Max = 10**5 +1
Mod = 10**9 +7

t,k = map(int, input().split())

prfx = [1] * Max
prfx[0] = 0

prfx[k] = 2


for i in range(k+1,Max):
    prfx[i] = (prfx[i-1] + prfx[i-k])%Mod
    
    
for i in range(k+1,Max):
    prfx[i] = (prfx[i-1] + prfx[i - k]) % Mod
    
    
for i in range(1,Max):
    prfx[i] = (prfx[i] + prfx[i-1]) % Mod
    
for _ in range(t):
    a,b = map(int,input().split())
    
    print((prfx[b] - prfx[a-1]) % (10**9 + 7))