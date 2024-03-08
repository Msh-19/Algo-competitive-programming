class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        right = -inf

        for k in nums[::-1]:
            if k < right:
                return True
            while stack and stack[-1]<k:
                right = stack.pop()
            stack.append(k)
        return False