# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution(object):
    def minFallingPathSum(self, matrix):
        row,col = len(matrix),len(matrix[0])

        @cache
        def dfs(i,j):
            val = 0
            if j<0 or j>=len(matrix):
                return inf
            if i == row - 1:
              return matrix[i][j]
            return min(dfs(i+1,j-1),dfs(i+1,j),dfs(i+1,j+1)) + matrix[i][j]
        val = inf
        for i in range(row):
            val = min(val, dfs(0,i))
        return val 