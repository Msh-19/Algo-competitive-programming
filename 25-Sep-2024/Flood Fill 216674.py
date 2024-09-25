# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        org_color = image[sr][sc]
        if org_color == color:
            return image
        visited = set()
        res = []
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or image[i][j] != org_color or (i,j) in visited:
                return
            visited.add((i,j))
            image[i][j] = color
            for dr,dc in dirs:
                nrow,ncol = i+dr,j+dc
                dfs(nrow,ncol)
        
        dfs(sr,sc)
        
        return image