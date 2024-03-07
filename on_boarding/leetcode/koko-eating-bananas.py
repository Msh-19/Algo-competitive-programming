class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def checker(mid):
            hour = 0
            for banana in piles:
                hour += banana//mid
                hour += 1 if banana%mid != 0 else 0
            return hour <= h
        
        left = 1
        right = max(piles)

        while left+1 < right:
            mid = (left+right)//2
            if checker(mid):
                right = mid
            else:
                left = mid
        
        return left if checker(left) else right

    