# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        left,right = 0, start[-1]+d

        def check(dist):
            cur = start[0]

            for s in start[1:]:
                if cur + dist > s + d:
                    return False
                
                cur = max(cur + dist,s)
            return True

        while left <= right:
            mid = left + (right - left) //2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1