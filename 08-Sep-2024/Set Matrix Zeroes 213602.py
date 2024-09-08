# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(mat)
        cols = len(mat[0])
        fcol = False
        frow = False

        for i in range(rows):
            if mat[i][0] == 0:
                fcol = True
        
        for i in range(cols):
            if mat[0][i] == 0:
                frow = True

        for i in range(1,rows):
            for j in range(1,cols):
                if mat[i][j] == 0:
                    mat[0][j] = mat[i][0] = 0

        for i in range(1,rows):
            if mat[i][0] == 0:
                for j in range(1,cols):
                    mat[i][j] = 0


        for j in range(1,cols):
            if mat[0][j] == 0:
                for i in range(1,rows):
                    mat[i][j] = 0
        
        if fcol:
            for i in range(rows):
                mat[i][0] = 0
        
        if frow:
            for j in range(cols):
                mat[0][j] = 0