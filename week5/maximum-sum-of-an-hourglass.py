class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        max_sum = float("-inf")

        for i in range(row - 2):
            for j in range(column - 2):
                current_sum = (
                grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
                grid[i + 1][j + 1] +
                grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
            )
            
                max_sum = max(max_sum,current_sum)

        return max_sum