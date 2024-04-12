# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, -1),
            (1, 1),
            (-1, 1),
            (-1, -1),
        ]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] != 0:
            return -1
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))

        while q:
            count += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if (i, j) == (rows - 1, cols - 1):
                    return count
                for dr, dc in directions:
                    r = i + dr
                    c = j + dc
                    if inbound(r, c) and (r, c) not in visited and grid[r][c] == 0:
                        q.append((r, c))
                        visited.add((r, c))
        return -1
