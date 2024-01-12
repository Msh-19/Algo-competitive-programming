class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1


        if not nums:
            return 0
        if len(nums) == 1: 
            if nums[0] == val:
                return left
            else:
                return left + 1
        while left < right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[right] == val:
                right -= 1
            elif nums[left] != val:
                left += 1

        if nums[left] == val:
            return left

        return left + 1