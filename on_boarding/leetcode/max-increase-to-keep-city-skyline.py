class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rows = [0]*n
        cols = [0]*n

        for r in range(n):
            for c in range(n):
                rows[r] = max(rows[r],grid[r][c])
                cols[c] = max(cols[c],grid[r][c])

        total = 0
        for r in range(n):
            for c in range(n):
                total += max(min(rows[r],cols[c]) - grid[r][c],0)
        return total