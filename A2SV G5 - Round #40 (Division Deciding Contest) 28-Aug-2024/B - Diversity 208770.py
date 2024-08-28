# Problem: B - Diversity - https://codeforces.com/gym/543431/problem/B

from collections import Counter
li = input()

count = Counter(li)
t = int(input())


res = t-len(count)
if len(li) < t:
    print("impossible")
else:
    if res < 0:
        print(0)
    else:
        print(res)

