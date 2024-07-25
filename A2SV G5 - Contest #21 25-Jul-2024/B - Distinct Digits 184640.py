# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

t = int(input())
for _ in range(t):
    nums = []
    num = int(input())
    
    for digit in range(9,0,-1):
        if num >=digit:
            nums.append(digit)
            num -= digit
            
    nums.sort()
    
    res = ''.join(map(str,nums))
    print(res)