from collections import Counter
# use the a[j] - a[i] = j - i
T = int(input())

for _ in range(T):
    cursum = 0
    totalsum = 0

    n = int(input())
    li = list(map(int,input()))
    prefix = [0]
    for num in li:
        cursum += num
        prefix.append(cursum)    
    for i in range(len(prefix)):
        prefix[i] -= i
    count = Counter(prefix)

    for val in count.values():
        totalsum += (val*(val-1))//2

        

    print(totalsum)