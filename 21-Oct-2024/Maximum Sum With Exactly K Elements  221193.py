# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        for _ in range(k):
            res += nums[-1]
            nums[-1]+=1
        return res