# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        path = set()
        
        def travel(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or r>=row or c>=col or word[i]!=board[r][c] or
            (r,c) in path):
                return False

            path.add((r,c))
            output = (travel(r+1,c,i+1) or travel(r-1,c,i+1) or travel(r,c+1,i+1) or travel(r,c-1,i+1))
            path.remove((r,c))

            return output

        for r in range(row):
            for c in range(col):
                if travel(r,c,0): return True

        return False