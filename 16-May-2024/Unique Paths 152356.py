# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [ [i for i in range(n)] for i in range(m)]

        dp[0] = [1]*n
        for k in range(m):
            dp[k][0] = 1  
        
        dp[0][0] = 1

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]

                    
