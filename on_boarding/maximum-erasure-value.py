class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 1
        max_score = nums[left]
        current_score = nums[left]
        unique_set = set([nums[left]])

        while right < len(nums):
            if nums[right] not in unique_set:
                unique_set.add(nums[right])
                current_score += nums[right]
                max_score = max(max_score, current_score)
                right += 1
            else:
                unique_set.remove(nums[left])
                current_score -= nums[left]
                left += 1

        return max_score