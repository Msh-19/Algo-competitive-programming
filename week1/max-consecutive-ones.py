class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0
        for elem in nums:
            if elem == 0:
                current_consecutive = 0
            else:
                current_consecutive += 1
                if current_consecutive > max_consecutive:
                    max_consecutive = current_consecutive
        return max_consecutive