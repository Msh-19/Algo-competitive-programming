class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        

        for r in range(row):
            for c in range(r,row):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for rows in matrix:
            rows.reverse()

        