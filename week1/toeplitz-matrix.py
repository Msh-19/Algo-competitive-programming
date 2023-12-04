class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        columns = len(matrix[0])
        rows = len(matrix)

        for i in range(1,rows):
            for j in range(1,columns):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
