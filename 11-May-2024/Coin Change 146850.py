# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(target):
            if target == 0:
                return 0
            if target < 0:
                return -1

            if target in memo:
                return memo[target]

            min_coins = float('inf')
            for coin in coins:
                result = dp(target - coin)
                if result >= 0:
                    min_coins = min(min_coins,result +1)

            memo[target] = min_coins if min_coins != float("inf") else -1
            return memo[target]

        return dp(amount)