# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [0]*n
        dp[-1] = 1 if obstacleGrid[-1][-1] == 0 else 0
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c+1 < n:
                    dp[c] = dp[c] + dp[c+1]
        return dp[0]