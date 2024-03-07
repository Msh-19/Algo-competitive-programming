class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        original_idx = {intervals[i][0]:i for i in range(n)}
        starts = [intervals[i][0] for i in range(n)]
        starts.sort()
        ans = []

        for i in range(n):
            pos = bisect_left(starts,intervals[i][1])

            if pos == n:
                ans.append(-1)
            else:
                ans.append(original_idx[starts[pos]])
        
        return ans