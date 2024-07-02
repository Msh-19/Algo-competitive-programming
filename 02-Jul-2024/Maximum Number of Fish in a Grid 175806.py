# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        def bfs(i, j):
            fish = 0
            q = [(i, j)]
            seen.add((i, j))
            for r, c in q:
                fish += grid[r][c]
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))
            return fish
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in seen:
                    res = max(res, bfs(i, j))
        return res
                    
                        
                
        