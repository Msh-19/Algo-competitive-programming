# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            if (num - difference) in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
        return max(dp.values())