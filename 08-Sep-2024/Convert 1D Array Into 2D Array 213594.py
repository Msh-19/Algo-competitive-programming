# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        result = [[0]*n for _ in range(m)]

        for i in range(len(original)):
            row, col = divmod(i,n)
            result[row][col] = original[i]

        return result