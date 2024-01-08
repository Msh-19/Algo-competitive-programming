class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = maxsize
        currentSum = 0

        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                min_length = min(min_length, right - left + 1)
                currentSum -= nums[left]
                left += 1

        return min_length if min_length != maxsize else 0