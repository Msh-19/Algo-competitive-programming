class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        countO = 0
        countC = 0
        ans = 0

        for i in s:
            if i == "(":
                countO += 1
            elif i == ")":
                if countO > 0:
                    countO -= 1
                else: 
                    countC += 1
        ans = countO + countC
        return ans