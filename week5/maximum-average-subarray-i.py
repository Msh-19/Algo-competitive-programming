class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        window_avg = window_sum/k
        maxwindow_sum = window_sum
        maxAvg = window_avg
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            maxwindow_sum = max(maxwindow_sum, window_sum)
        
        maxAvg = maxwindow_sum/k
            

        return maxAvg