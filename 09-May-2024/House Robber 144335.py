# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def work(ind, cur):
            if ind >= len(nums):
                return cur

            return max(work(ind + 1, cur), work(ind + 2, cur + nums[ind]))

        return work(0, 0)
