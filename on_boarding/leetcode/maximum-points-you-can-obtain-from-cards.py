class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        n = len(cardPoints)
        window_sum = sum(cardPoints[:n-k])
    
        min_window_sum = window_sum
        for i in range(n - k, n):
            window_sum += cardPoints[i] - cardPoints[i - (n - k)]
            min_window_sum = min(min_window_sum, window_sum)
        
        
        return total_points - min_window_sum