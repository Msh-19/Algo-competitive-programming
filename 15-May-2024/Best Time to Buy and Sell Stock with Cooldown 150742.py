# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        memo = {}

        def dp(i, holding, cooldown):
            if i >= n:
                return 0

            if (i,holding,cooldown) in memo:
                return memo[(i,holding,cooldown)]

            no_action = dp(i+1,holding,cooldown)

            if holding:
                sell = dp(i+2,False,True) + prices[i]
                memo[(i,holding,cooldown)] = max(sell,no_action)
            else:
                buy = dp(i+1,True,cooldown) - prices[i]
                memo[(i,holding,cooldown)] = max(buy,no_action)

            return memo[(i,holding,cooldown)]

        return dp(0, False, False)
