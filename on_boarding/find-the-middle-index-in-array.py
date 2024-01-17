class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = []
        rightSum = []
        
        output = 0
        tSum = 0
        for i in range(len(nums)):
            tSum += nums[i]
            leftSum.append(tSum)

        ttSum = 0
        nums.reverse()
        for j in range(len(nums)):
            ttSum += nums[j]
            rightSum.append(ttSum)
        
        
        rightSum.reverse()
        print(leftSum)
        print(rightSum)
        for k in range(len(nums)):
            if leftSum[k] == rightSum[k]:
                output = k
                return output
        return -1
    