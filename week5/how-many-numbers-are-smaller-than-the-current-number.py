class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter +=1
            ans.append(counter)
        return ans