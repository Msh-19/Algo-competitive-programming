# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])

        mat = [[inf for i in range(n)] for j in range(m)]

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r == m-1 and c == n-1:
                    mat[r][c] = max(1,1 - dungeon[r][c])
                elif r == m-1:
                    mat[r][c] = max(mat[r][c+1] - dungeon[r][c],1)
                elif c == n-1:
                    mat[r][c] = max(mat[r+1][c] - dungeon[r][c],1)
                else:
                    mat[r][c] = max(min(mat[r+1][c],mat[r][c+1]) - dungeon[r][c],1)
        
        return mat[0][0]
