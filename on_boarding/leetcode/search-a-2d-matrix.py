class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = -1
        right = len(matrix)*len(matrix[0])
        m = len(matrix)
        n = len(matrix[0])

        while left + 1 < right:
            mid = (left+right)//2
            midrow = mid // n
            midcol = mid % n

            if matrix[midrow][midcol] == target:
                return True
            elif matrix[midrow][midcol] > target:
                right = mid
            else:
                left = mid

        return False

            