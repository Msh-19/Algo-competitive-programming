# Problem: A - A2SV Contest #25 - https://codeforces.com/gym/535749/problem/A

pv,pm,vt,mt = (map(int, input().split()))

v = max((3*pv)/10,pv - (pv/250)*vt)
m = max((3*pm)/10,pm - (pm/250)*mt)


if v > m:
    print("Misha")
elif v < m:
    print("Vasya")
else:
    print("Tie")