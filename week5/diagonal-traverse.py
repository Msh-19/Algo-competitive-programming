class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        defit = defaultdict(list)
        row = len(mat)
        column = len(mat[0])
        ans = []
        for r in range(row):
            for c in range(column):
                defit[r+c].append(mat[r][c])
        for key in defit:
            if key%2 == 0:
                defit[key].reverse()
        
        for key in defit:
            ans.extend(defit[key])
        return ans
        