# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}


        tpath = [False]*366
        for k in days:
            tpath[k] = True

        def dp(i):
            if i>365:
                return 0

            if i in memo:
                return memo[i]
            else:
                if tpath[i] == True:
                    memo[i] = min(costs[0] + dp(i+1), costs[1] + dp(i+7), costs[2] + dp(i+30))
                else:
                    memo[i] = dp(i+1)
                return memo[i]

        return dp(days[0])
