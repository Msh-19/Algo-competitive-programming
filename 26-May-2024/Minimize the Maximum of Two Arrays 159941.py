# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        low = 1
        high = 10 ** 29
        ans = 0 

        def valid(num , low):
            return (num - num // divisor1) >= uniqueCnt1 and (num - num // divisor2) >= uniqueCnt2 and (num - num // lcm(divisor1 , divisor2)) >= (uniqueCnt2 + uniqueCnt1)


        while low <= high:
            mid = (low + high) // 2

            if valid(mid, low):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans