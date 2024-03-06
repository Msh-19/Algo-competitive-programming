# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n+1
        temp = 0
        while left+1 < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                temp = mid
                right = mid
            else:
                left = mid 
        return temp
                