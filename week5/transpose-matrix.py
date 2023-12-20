class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        output = [[0]*row for _ in range(column)]   
        for c in range(column):
            output[c] = []
            for r in range(row):
                output[c].append(matrix[r][c])

        return output