# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        val = sum(nums)
        target = val //2
        if val%2 != 0:
            return False

        memo = {}
        def recur(i,sums):
            if sums == 0:
                return True

            if i>=len(nums) or sums <0:
                return False

            
            if (i,sums) not in memo:
                memo[(i,sums)] = recur(i+1,sums) or recur(i+1,sums-nums[i])
            return memo[(i,sums)]
        return recur(0,target)
