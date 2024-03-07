class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        output = 0
        for k in range(2,n):
            i,j = 0,k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    output += j-i
                    j -= 1
                else:
                    i+=1
        return output
                