# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = [set() for i in range(len(stones))]
        dp[0] = set([1])
        for i in range(1,len(stones)):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff in dp[j]:
                # if it does, update the corresponding index on the list positon
                    dp[i].update([diff,diff-1,diff+1])
        if dp[-1]:
            return True
        else:
            return False
