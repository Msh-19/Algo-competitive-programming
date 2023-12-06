class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        size = 3
        n = len(num)
        ans = ""
        hiAns = ""
        for i in range(n-2):
            if num[i] == num[i+1] == num[i+2]:
                ans = num[i:i+3]
                if ans > hiAns:
                    hiAns = ans

        return hiAns

        