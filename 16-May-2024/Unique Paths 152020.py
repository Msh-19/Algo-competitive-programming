# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(x,y):
            if (x,y) in memo:
                return memo[(x,y)]

            if x == m-1 and y == n-1:
                return 1

            if x == m or y == n:
                return 0

            right_paths = dfs(x+1,y)
            down_paths = dfs(x,y+1)

            memo[(x,y)] = right_paths + down_paths
            return memo[(x,y)]

        return dfs(0,0)