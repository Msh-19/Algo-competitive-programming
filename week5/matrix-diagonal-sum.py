class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        row = len(mat)
        col = len(mat[0])
        primeD = []
        reverseD = []
        delr = 0
        delc = 0
        if (row*col)%2 == 1:
            delr = row//2
            delc = col//2

        for r in range(row):
            for c in range(col):
                if r-c == 0:
                    primeD.append(mat[r][c])
                if r+c == row-1:
                    if delr == r and delc == c:
                        continue
                    reverseD.append(mat[r][c])


        
        print(primeD)
        print(reverseD)
        return sum(primeD) + sum(reverseD)
                     