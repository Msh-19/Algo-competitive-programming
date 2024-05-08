# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        c = 0
        for i,j in enumerate(nums):
            for x in range(i,len(nums)):
                j = gcd(j,nums[x])

                if j<k:
                    break
                if j == k:
                    c+=1
        return c