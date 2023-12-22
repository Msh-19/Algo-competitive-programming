class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])
        count = 0
        for c in range(col):
            for r in range(row-1):
                if strs[r][c] > strs[r+1][c]:
                    count+=1
                    break
        return count
        