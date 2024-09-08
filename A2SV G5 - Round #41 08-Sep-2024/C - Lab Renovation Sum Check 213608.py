# Problem: C - Lab Renovation Sum Check - https://codeforces.com/gym/545013/problem/C

t = int(input())
mat = []
for _ in range(t):
    mat.append(list(map(int,input().split())))

flag = True

for r in range(t):
    for c in range(t):
        if mat[r][c]!= 1:
            sums = []
            for i1 in range(t):
                for j1 in range(t):
                    sums.append(mat[i1][c] + mat[r][j1])
            if mat[r][c] not in sums:
                flag = False
if flag:
    print("Yes")
else:
    print("No")