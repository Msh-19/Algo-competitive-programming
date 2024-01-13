class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = [[False]*9 for _ in range(9)]
        m2 = [[False]*9 for _ in range(9)]
        m3 = [[False]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i//3 * 3+j//3

                    if m[i][num] or m2[j][num] or m3[k][num]:
                        return False

                    m[i][num] = m2[j][num] = m3[k][num] = True

        return True