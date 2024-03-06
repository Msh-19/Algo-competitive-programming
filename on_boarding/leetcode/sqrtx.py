class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = -1, x+1
        while left+1 < right:
            mid = (left + right)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid
            else:
                right = mid

        return left