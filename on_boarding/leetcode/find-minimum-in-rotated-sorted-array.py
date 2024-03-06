class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right= len(nums)-1 
       
        if nums[left] <= nums[right]:
            return nums[0]

        while left+1 < right:
            mid = (left + right)//2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        
        return min(nums[left],nums[right])

        
            