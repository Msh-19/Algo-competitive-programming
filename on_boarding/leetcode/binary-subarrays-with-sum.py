class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        current_sum = 0
        sums_map = {0: 1}
        
        for num in nums:
            current_sum += num
            count += sums_map.get(current_sum - goal, 0)
            sums_map[current_sum] = sums_map.get(current_sum, 0) + 1
        
        return count