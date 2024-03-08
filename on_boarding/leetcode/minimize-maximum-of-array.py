class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        curmax = nums[0]
        totalsum = nums[0]

        for i in range(1,n):
            totalsum += nums[i]
            value = (totalsum + i) // (i + 1)
            curmax = max(curmax, value)

        return curmax
