class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numberss = set(nums)
        max_length = 0 
        current_length = 0

        while max_length < len(numberss):
            num = numberss.pop()
            longest = num+1
            while longest in numberss:
                numberss.remove(longest)
                longest += 1
            num = num -1
            while num in numberss:
                numberss.remove(num)
                num -= 1
            max_length = max(max_length, longest-num-1)
        return max_length