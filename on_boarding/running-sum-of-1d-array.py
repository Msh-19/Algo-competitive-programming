class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        currSum = nums[0]
        output.append(nums[0])
        for i in range(1,len(nums)):
            currSum += nums[i]
            output.append(currSum)

        return output
