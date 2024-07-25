# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

t = int(input())

st = input()
res = ""

i=0
while i<t:
    res+=st[i]
    i+= len(res)
print(res)