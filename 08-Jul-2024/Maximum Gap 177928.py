# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0

        nums.sort()
        diff = 0

        for i in range(1,len(nums)):
            diff = max(diff, nums[i] - nums[i-1])

        return diff