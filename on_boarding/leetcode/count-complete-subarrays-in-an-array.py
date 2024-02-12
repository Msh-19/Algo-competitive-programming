class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        complete = 0
        n = len(nums)
        k = len(set(nums))
        
        for i in range(n):
            subarrSet = set()

            for j in range(i, n):
                subarrSet.add(nums[j])

                if len(subarrSet) == k:
                    complete += 1
        
        return complete