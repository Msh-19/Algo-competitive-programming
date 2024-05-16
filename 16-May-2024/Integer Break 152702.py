# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        dp = [0]*(n+1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3,n+1):
            max_product = 0

            for j in range(1,i//2 + 1):
                product = j*(i-j)

                max_product = max(max_product,product,j*dp[i - j])
            
            dp[i] = max_product

        return dp[n]