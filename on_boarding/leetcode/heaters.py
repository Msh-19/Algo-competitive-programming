class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        m = len(houses)
        n = len(heaters)


# checks for when a value streches out to find possible coverage
# The mid value is the radius we are trying to find in the lists
        def check(mid):
            p1, p2 = 0, 0
            while p1 < m and p2 < n:
                low = heaters[p2] - mid
                high = heaters[p2] + mid
                if houses[p1] <= high and houses[p1] >= low:
                    p1 += 1
                else:
                    p2 += 1
            if p1 == m:
                return True
            else:
                return False

        left = -1
        right = 10**9 + 1

        while left + 1 < right:
            mid = (left + right) // 2


            if check(mid):
                right = mid
            else:
                left = mid

        return right
