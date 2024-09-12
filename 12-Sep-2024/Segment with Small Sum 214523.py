# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,s = map(int,input().split())

li = list(map(int, input().split()))
maxSum = 0

l = 0
curr_sum = 0
max_len = 0

for r in range(len(li)):
    curr_sum += li[r]
    
    while curr_sum > s and l <=r:
        curr_sum -= li[l]
        l+=1
        
    max_len = max(max_len,r - l + 1)

print(max_len)
