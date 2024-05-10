# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def recur(ind,val):
            
            if ind == len(nums) and val == target:
                return 1
            if ind == len(nums) and val != target:
                return 0


            res = recur(ind+1,nums[ind]+val) + recur(ind+1, val - nums[ind])
            return res
        return recur(0,0)