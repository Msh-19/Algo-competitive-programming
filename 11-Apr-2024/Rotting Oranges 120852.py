# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        minute = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
            direc = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in direc:
                    row, col = dr+r, dc+c 
                    if (row < 0 or row == rows or col<0 or col == cols or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            minute += 1

        return minute if fresh == 0 else -1