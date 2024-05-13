# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for i in range(len(prices)):
            prevcash = cash
            cash = max(cash,hold + prices[i] - fee)
            hold = max(hold, prevcash - prices[i])
        return cash