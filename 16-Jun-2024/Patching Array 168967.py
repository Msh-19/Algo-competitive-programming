# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cursum = 1
        patch = 0
        index = 0

        while cursum <= n:
            if index < len(nums) and nums[index] <= cursum:
                cursum += nums[index]
                index += 1
            else:
                cursum += cursum
                patch += 1

        return patch