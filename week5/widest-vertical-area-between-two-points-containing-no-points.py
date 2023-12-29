class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_pairs = sorted(points, key=lambda x: x[0])
        
        maxdiff = 0
        for i in range(len(sorted_pairs)-1):
            diff = sorted_pairs[i+1][0] - sorted_pairs[i][0]

            maxdiff = max(maxdiff, diff)

        return maxdiff