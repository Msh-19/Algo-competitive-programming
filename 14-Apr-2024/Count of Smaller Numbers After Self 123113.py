# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList()
        result = []

        for i in range(len(nums) -1, -1,-1):
            num = nums[i]

            idx = sorted_list.bisect_left(num)
            result.append(idx)
            sorted_list.add(num)

        return result[::-1]