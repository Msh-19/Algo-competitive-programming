# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        size = len(nums)

        if size <= 4:
            return 0

        nums.sort()

        min_diff = inf

        for left in range(4):
            right = size - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])

        return min_diff