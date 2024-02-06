class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalSum = sum(nums)
        targetRemainder = totalSum % p
        
        if targetRemainder == 0:
            return 0
        
        remainderIndex = {0: -1}
        currentRemainder = 0
        minLength = float('inf')

        for i, num in enumerate(nums):
            currentRemainder = (currentRemainder + num) % p
            complementRemainder = (currentRemainder - targetRemainder + p) % p

            if complementRemainder in remainderIndex:
                minLength = min(minLength, i - remainderIndex[complementRemainder])

            remainderIndex[currentRemainder] = i

        return minLength if minLength != float('inf') and minLength < len(nums) else -1