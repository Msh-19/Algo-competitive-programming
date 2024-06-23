# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m,n = len(matrix),len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        indegrees = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    ni,nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegrees[ni][nj] += 1
        
        queue = deque()

        for i in range(m):
            for j in range(n):
                if indegrees[i][j] == 0:
                    queue.append((i,j))

        longest_path = 0
        while queue:
            longest_path += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                        indegrees[nx][ny] -= 1
                        if indegrees[nx][ny] == 0:
                            queue.append((nx,ny))

        return longest_path