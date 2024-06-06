# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        queue = deque()
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True
        
        steps = 0
        result = [[-1] * m for _ in range(n)]

        while queue:
            k = len(queue)

            for _ in range(k):
                r, c = queue.popleft()
                result[r][c] = steps

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = r + dr, c + dc

                    if x < 0 or y < 0 or x >= n or y >= m or visited[x][y]:
                        continue
                    
                    visited[x][y] = True
                    queue.append((x, y))
            
            steps += 1
        
        return result
